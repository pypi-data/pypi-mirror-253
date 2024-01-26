from ..Types import AcquisitionType, Timepoint
from . import SequenceModule, AcquisitionModule, Register
import numpy as np
import torch

@Register
class TRUEFISPAcquisitionModule(AcquisitionModule):
    """
    Class representing a TRUEFISP acquisition module.

    Args:
        timepoints (np.array, optional): Array of timepoints. Defaults to [].
        units (SequenceUnits, optional): The units of the module. Defaults to None.
    """
    def __init__(self, timepoints=[], units=None):
        """
        Initialize a TRUEFISPAcquisitionModule instance.

        Args:
            timepoints (np.array, optional): Array of timepoints. Defaults to [].
            units (SequenceUnits, optional): The units of the module. Defaults to None.
        """
        AcquisitionModule.__init__(self, acquisitionType=AcquisitionType.TRUEFISP, timepoints=timepoints, units=units) 

    def __str__(self):
        """
        Generate a string representation of the module.

        Returns:
            str: The string representation of the module.
        """
        return SequenceModule.__str__(self) + " || Acquisition Type: " + self.acquisitionType.name + " || Timepoints: \n" + str(self.timepoints)
    
    def __dict__(self):
        """
        Generate a dictionary representation of the module.

        Returns:
            dict: The dictionary representation of the module.
        """
        timepointDict = [dict(zip(self.timepoints.dtype.names,x.tolist())) for x in self.timepoints]
        moduleDict  = {
            "type": str(self.__class__.__name__),
            "timepoints": timepointDict
        }
        return moduleDict
    
    @staticmethod
    def FromJson(jsonInput):
        """
        Create an instance of TRUEFISPAcquisitionModule from JSON input.

        Args:
            jsonInput (dict): The JSON input data.

        Returns:
            TRUEFISPAcquisitionModule: An instance of TRUEFISPAcquisitionModule.
        """
        timepointsJson = jsonInput.get("timepoints")
        if(timepointsJson != None):
            timepoints = []
            for timepointJson in timepointsJson:
                timepoints.append(tuple(timepointJson.values()))
            timepoints = np.array(timepoints, dtype=Timepoint)         
            return TRUEFISPAcquisitionModule(timepoints) 
        else:
            print("TRUEFISPAcquisitionModule requires timepoints")
    
    def Simulate(self, dictionaryEntries, numSpins, device=None, inputMx=None, inputMy=None, inputMz=None): 
        """
        Simulate the TRUEFISP acquisition module.

        Args:
            dictionaryEntries (dict): Dictionary containing relaxation parameters.
            numSpins (int): Number of spins to simulate.
            device (torch.device, optional): The device for simulation. Defaults to None.
            inputMx (torch.Tensor, optional): Input magnetization in x direction. Defaults to None.
            inputMy (torch.Tensor, optional): Input magnetization in y direction. Defaults to None.
            inputMz (torch.Tensor, optional): Input magnetization in z direction. Defaults to None.

        Returns:
            tuple: A tuple containing simulation time and magnetization tensors.
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
        Mx0 = torch.zeros((numTimepoints, numSpins, numDictionaryEntries))
        My0 = torch.zeros((numTimepoints, numSpins, numDictionaryEntries))
        Mz0 = torch.zeros((numTimepoints, numSpins, numDictionaryEntries))
        Time = torch.zeros((numTimepoints))

        Mx = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        My = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        Mz = torch.zeros((numSpins, numDictionaryEntries)).to(device)    
        FAs = torch.deg2rad(FAs)
        PHs = torch.deg2rad(PHs)
        
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
                del fa, tr, te, tre, At2te, At1te, Bt1te, At2tr, At1tr, Bt1tr, Mxi, Myi, Mzi
        del T1s, T2s, B1s, FAs, PHs, Mx, My, Mz
        return Time,Mx0,My0,Mz0