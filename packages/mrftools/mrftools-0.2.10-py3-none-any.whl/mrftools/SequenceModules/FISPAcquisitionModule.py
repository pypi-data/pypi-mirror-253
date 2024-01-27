from ..Types import AcquisitionType, Timepoint
from . import SequenceModule, AcquisitionModule, Register
import numpy as np
import torch


@Register
class FISPAcquisitionModule(AcquisitionModule):
    """
    A module representing Fast Imaging with Steady-state Precession (FISP) acquisition in a sequence.

    Args:
        timepoints (array-like, optional): List of timepoints. Defaults to an empty list.
        dephasingRange (float, optional): Dephasing range in degrees. Defaults to 360.
        units (SequenceUnits, optional): The units of time. Defaults to None.
    """
    def __init__(self, timepoints=[], dephasingRange=360, units=None):
        """
        Initialize an FISPAcquisitionModule instance.

        Args:
            timepoints (array-like, optional): List of timepoints. Defaults to an empty list.
            dephasingRange (float, optional): Dephasing range in degrees. Defaults to 360.
            units (SequenceUnits, optional): The units of time. Defaults to None.
        """
        AcquisitionModule.__init__(self, acquisitionType=AcquisitionType.FISP, timepoints=timepoints, units=units) 
        self.dephasingRange = dephasingRange

    def __str__(self):
        """
        Return a string representation of the module.

        Returns:
            str: A formatted string representation.
        """
        return SequenceModule.__str__(self) + " || Acquisition Type: " + self.acquisitionType.name + " || Dephasing Range (# of pi): " + f'{self.dephasingRange/np.pi:7.5f}' + " || Timepoints: \n" + str(self.timepoints)
    
    def __dict__(self):
        """
        Return a dictionary representation of the module.

        Returns:
            dict: A dictionary containing module information.
        """
        timepointDict = [dict(zip(self.timepoints.dtype.names,x.tolist())) for x in self.timepoints]
        moduleDict  = {
            "type": str(self.__class__.__name__),
            "timepoints": timepointDict,
            "dephasingRange":self.dephasingRange
        }
        return moduleDict

    @staticmethod
    def FromJson(jsonInput):
        """
        Create an FISPAcquisitionModule instance from a JSON input.

        Args:
            jsonInput (dict): The JSON input containing module information.

        Returns:
            FISPAcquisitionModule: The created FISPAcquisitionModule instance.
        """
        dephasingRange = jsonInput.get("dephasingRange")
        timepointsJson = jsonInput.get("timepoints")
        if(dephasingRange != None and timepointsJson != None):
            timepoints = []
            for timepointJson in timepointsJson:
                timepoints.append(tuple(timepointJson.values()))
            timepoints = np.array(timepoints, dtype=Timepoint)         
            return FISPAcquisitionModule(timepoints, dephasingRange)   
        else:
            print("FISPAcquisitionModule requires dephasingRange and timepoints")

    def Simulate(self, dictionaryEntries, numSpins, device=None, inputMx=None, inputMy=None, inputMz=None): 
        """
        Simulate FISP acquisition for a given set of dictionary entries.

        Args:
            dictionaryEntries (dict): A dictionary containing T1, T2, and B1 values.
            numSpins (int): The number of spins to simulate.
            device (torch.device, optional): The device to perform the simulation on. Defaults to None.
            inputMx (torch.Tensor, optional): Input Mx values for simulation. Defaults to None.
            inputMy (torch.Tensor, optional): Input My values for simulation. Defaults to None.
            inputMz (torch.Tensor, optional): Input Mz values for simulation. Defaults to None.

        Returns:
            tuple: A tuple containing the simulation results (Time, Mx0, My0, Mz0).
        """
        if(device==None):
            if torch.cuda.is_available():
                device = torch.device("cuda")
            else:
                device = torch.device("cpu")    
        T1s = torch.tensor(dictionaryEntries['T1']).to(device)
        T2s = torch.tensor(dictionaryEntries['T2']).to(device)
        B1s = torch.tensor(dictionaryEntries['B1']).to(device)
        TRs = torch.tensor(self.timepoints['TR'].copy()).to(device)
        TEs = torch.tensor(self.timepoints['TE'].copy()).to(device)
        FAs = torch.tensor(self.timepoints['FA'].copy()).to(device)
        PHs = torch.tensor(self.timepoints['PH'].copy()).to(device)

        numTimepoints = len(self.timepoints); numDictionaryEntries = len(dictionaryEntries)
        phaseValues = np.linspace(-1*self.dephasingRange/2, self.dephasingRange/2, numSpins)

        spinOffresonances = torch.tensor(phaseValues).to(device)
        spinOffresonances = torch.deg2rad(spinOffresonances)
        FAs = torch.deg2rad(FAs)
        PHs = torch.deg2rad(PHs)

        Mx0 = torch.zeros((numTimepoints, numSpins, numDictionaryEntries))
        My0 = torch.zeros((numTimepoints, numSpins, numDictionaryEntries))
        Mz0 = torch.zeros((numTimepoints, numSpins, numDictionaryEntries))
        Time = torch.zeros((numTimepoints))

        Mx = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        My = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        Mz = torch.zeros((numSpins, numDictionaryEntries)).to(device)    

        phaseValueCosines = torch.cos(spinOffresonances)
        phaseValueSines = torch.sin(spinOffresonances)
        
        if(inputMx is not None):
            if(torch.numel(inputMx) == numSpins*numDictionaryEntries and torch.numel(inputMy) == numSpins*numDictionaryEntries and torch.numel(inputMz) == numSpins*numDictionaryEntries):
                Mx = inputMx
                My = inputMy
                Mz = inputMz
            else:
                if(torch.numel(inputMx) == 1 and torch.numel(inputMy) == 1 and torch.numel(inputMz) == 1 ):
                    Mx = torch.ones(numSpins, numDictionaryEntries) * inputMx
                    My = torch.ones(numSpins, numDictionaryEntries) * inputMy
                    Mz = torch.ones(numSpins, numDictionaryEntries) * inputMz
                else: 
                    print("Simulation Failed: Number of input magnetization states doesn't equal number of requested spins to simulate.")
                    return
                
        Mx = Mx.to(device);  My = My.to(device); Mz = Mz.to(device); 
        with torch.no_grad():
            accumulatedTime = 0
            for iTimepoint in range(numTimepoints):
                fa = FAs[iTimepoint] * B1s
                tr = TRs[iTimepoint]
                te = TEs[iTimepoint]
                ph = PHs[iTimepoint]
                tre = tr-te

                Time[iTimepoint] = accumulatedTime
                accumulatedTime = accumulatedTime + tr

                At2te = torch.exp(-1*te/T2s)
                At1te = torch.exp(-1*te/T1s)
                Bt1te = 1-At1te
                
                At2tr = torch.exp(-1*tre/T2s)
                At1tr = torch.exp(-1*tre/T1s)
                Bt1tr = 1-At1tr

                # M2 = Rphasep*Rflip*Rphasem*M1;       % RF effect  

                # Applying Rphasem = [cos(-iph) -sin(-iph) 0; sin(-iph) cos(-iph) 0; 0 0 1];  
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = torch.multiply(torch.cos(-ph),Mxi) - torch.multiply(torch.sin(-ph), Myi)
                My = torch.multiply(torch.sin(-ph),Mxi) + torch.multiply(torch.cos(-ph), Myi)
                Mz = Mzi

                # Applying flip angle = [1 0 0; 0 cos(randflip(ii)) -sin(randflip(ii)); 0 sin(randflip(ii)) cos(randflip(ii))];
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = Mxi
                My = torch.multiply(torch.cos(fa),Myi)-torch.multiply(torch.sin(fa),Mzi)
                Mz = torch.multiply(torch.sin(fa),Myi)+torch.multiply(torch.cos(fa),Mzi)

                # Applying Rphasep = [cos(iph) -sin(iph) 0; sin(iph) cos(iph) 0; 0 0 1];  
                Mxi = Mx; Myi = My; Mzi = Mz
                Mx = torch.multiply(torch.cos(ph),Mxi) - torch.multiply(torch.sin(ph), Myi)
                My = torch.multiply(torch.sin(ph),Mxi) + torch.multiply(torch.cos(ph), Myi)
                Mz = Mzi

                # Relaxation over TE
                Mx = torch.multiply(Mx, At2te)
                My = torch.multiply(My, At2te)
                Mz = torch.multiply(Mz, At1te)+Bt1te

                # Reading value after TE and before TRE 
                Mx0[iTimepoint,:,:]=Mx.cpu()
                My0[iTimepoint,:,:]=My.cpu()
                Mz0[iTimepoint,:,:]=Mz.cpu()

                # Relaxation over TRE (TR-TE) 
                Mx = Mx*At2tr
                My = My*At2tr
                Mz = Mz*At1tr+Bt1tr

                # Applying off-resonance to spins
                Mxi = Mx.t()
                Myi = My.t()
                Mx = (torch.multiply(phaseValueCosines,Mxi) - torch.multiply(phaseValueSines,Myi)).t()
                My = (torch.multiply(phaseValueSines,Mxi) + torch.multiply(phaseValueCosines,Myi)).t()
                del fa, tr, te, tre, At2te, At1te, Bt1te, At2tr, At1tr, Bt1tr, Mxi, Myi, Mzi
        del T1s, T2s, B1s, FAs, PHs, spinOffresonances, Mx, My, Mz
        return Time,Mx0,My0,Mz0 
