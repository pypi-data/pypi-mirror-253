from ..Types import RFType, SequenceUnits, Units
from . import RFPreparationModule, Register
import torch

@Register
class InversionModule(RFPreparationModule):
    """
    A module representing an inversion recovery preparation using RF pulse.

    Args:
        totalDuration (float): Total duration of the module in seconds.
        rfDuration (float, optional): Duration of the RF pulse in seconds. Defaults to 0.
        rfPhase (float, optional): RF phase in degrees. Defaults to 0.
        units (SequenceUnits, optional): The units of the module. Defaults to None.
    """
    def __init__(self, totalDuration, rfDuration=0, rfPhase=0, units=None):
        RFPreparationModule.__init__(self, rfType=RFType.INVERSION, units=units) 
        self.totalDuration = totalDuration   # Seconds
        self.rfDuration = rfDuration         # Seconds
        self.rfPhase = rfPhase               # Degrees -- should it be? Matches the timeseries spec
        if(rfDuration != None):
            self.rfDuration = rfDuration
        else:
            self.rfDuration = 0
        if(rfPhase != None):
            self.rfPhase = rfPhase
        else:
            self.rfPhase = 0

    def __str__(self):
        """
        Return a string representation of the module.

        Returns:
            str: A formatted string representation.
        """
        return RFPreparationModule.__str__(self) + " || Total Duration (s): " + f'{self.totalDuration:7.5f}'  + " || RF Duration (s): " + f'{self.rfDuration:7.5f}' + " || RF Phase (degrees): " + f'{self.rfPhase:7.5f}'
    
    def __dict__(self):
        """
        Convert the module to a dictionary representation.

        Returns:
            dict: A dictionary containing the module's attributes.
        """
        moduleDict  = {
            "type": str(self.__class__.__name__),
            "totalDuration": self.totalDuration,
            "rfDuration": self.rfDuration,
            "rfPhase": self.rfPhase
        }
        return moduleDict
    
    def ConvertUnits(self, targetUnits:SequenceUnits):
        """
        Convert the module's parameters to the specified units.

        Args:
            targetUnits (SequenceUnits): The target units for conversion.
        """
        if(self.units != targetUnits):
            self.totalDuration =  Units.Convert(self.totalDuration, self.units.time, targetUnits.time)
            self.rfDuration =  Units.Convert(self.rfDuration, self.units.time, targetUnits.time)
            self.rfPhase =  Units.Convert(self.rfPhase, self.units.angle, targetUnits.angle)
            self.units = targetUnits

    def CastToIntegers(self):
        """Cast relevant module parameters to integers."""
        self.totalDuration = int(self.totalDuration)
        self.rfDuration = int(self.rfDuration)
        self.rfPhase = int(self.rfPhase)
    
    def CastToFloats(self):
        """Cast relevant module parameters to floats."""
        self.totalDuration = float(self.totalDuration)
        self.rfDuration = float(self.rfDuration)
        self.rfPhase = float(self.rfPhase)

    @staticmethod
    def FromJson(jsonInput):
        """
        Create an InversionModule instance from a JSON input.

        Args:
            jsonInput (dict): A dictionary containing JSON input data.

        Returns:
            InversionModule: An instance of InversionModule.
        """
        totalDuration = jsonInput.get("totalDuration")
        rfDuration = jsonInput.get("rfDuration")
        rfPhase = jsonInput.get("rfPhase")      
        if (totalDuration != None):
            return InversionModule(totalDuration, rfDuration, rfPhase) 
        else:
            print("InversionModule requires totalDuration")

    def Simulate(self, dictionaryEntries, numSpins, device=None, inputMx=None, inputMy=None, inputMz=None): 
        """
        Simulate the module's effect on magnetization.

        Args:
            dictionaryEntries (dict): Dictionary containing relaxation parameters.
            numSpins (int): Number of spins.
            device (torch.device, optional): The device to run the simulation on. Defaults to None.
            inputMx (torch.Tensor, optional): Input magnetization in the x-direction. Defaults to None.
            inputMy (torch.Tensor, optional): Input magnetization in the y-direction. Defaults to None.
            inputMz (torch.Tensor, optional): Input magnetization in the z-direction. Defaults to None.

        Returns:
            tuple: A tuple containing timepoints, Mx0, My0, and Mz0.
        """
        if(device==None):
            if torch.cuda.is_available():
                device = torch.device("cuda")
            else:
                device = torch.device("cpu")    
        T1s = torch.tensor(dictionaryEntries['T1']).to(device)
        T2s = torch.tensor(dictionaryEntries['T2']).to(device)
        B1s = torch.tensor(dictionaryEntries['B1']).to(device)

        numDictionaryEntries = len(dictionaryEntries)
        Mx0 = torch.zeros((1, numSpins, numDictionaryEntries))
        My0 = torch.zeros((1, numSpins, numDictionaryEntries))
        Mz0 = torch.zeros((1, numSpins, numDictionaryEntries))
        Time = torch.zeros((1))

        Mx = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        My = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        Mz = torch.zeros((numSpins, numDictionaryEntries)).to(device)    
        FA = torch.deg2rad(torch.tensor(180))
        PH = torch.deg2rad(torch.tensor(self.rfPhase))
        TR = self.totalDuration - self.rfDuration # Only allow for relaxation in the wait time after the RF is applied
            
        if(inputMx is not None):
            if(torch.numel(inputMx) == numSpins*numDictionaryEntries and torch.numel(inputMy) == numSpins*numDictionaryEntries and torch.numel(inputMz) == numSpins*numDictionaryEntries):
                Mx = inputMx
                My = inputMy
                Mz = inputMz
            else:
                if(torch.numel(inputMx) == 1 and torch.numel(inputMy) == 1 and torch.numel(inputMz) == 1 ):
                    Mx = (torch.ones(numSpins, numDictionaryEntries) * inputMx)
                    My = (torch.ones(numSpins, numDictionaryEntries) * inputMy)
                    Mz = (torch.ones(numSpins, numDictionaryEntries) * inputMz)
                else: 
                    print("Simulation Failed: Number of input magnetization states doesn't equal number of requested spins to simulate.")
                    return
        else:
            Mx = torch.zeros(numSpins, numDictionaryEntries)
            My = torch.zeros(numSpins, numDictionaryEntries)
            Mz = torch.ones(numSpins, numDictionaryEntries)

        Mx = Mx.to(device);  My = My.to(device); Mz = Mz.to(device); 

        with torch.no_grad():
                fa = FA
                tr = TR
                ph = PH
                At2tr = torch.exp(-1*tr/T2s)
                At1tr = torch.exp(-1*tr/T1s)
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

                # Relaxation over prep duration
                Mx = torch.multiply(Mx, At2tr)
                My = torch.multiply(My, At2tr)
                Mz = torch.multiply(Mz, At1tr)+Bt1tr

                # Reading value after TR and before TRE 
                Mx0[0,:,:]=Mx.cpu()
                My0[0,:,:]=My.cpu()
                Mz0[0,:,:]=Mz.cpu()
                Time[0] = self.totalDuration

                del fa, tr, At2tr, At1tr, Bt1tr, Mxi, Myi, Mzi
        del T1s, T2s, B1s, FA, TR, PH, Mx, My, Mz
        return Time,Mx0,My0,Mz0
