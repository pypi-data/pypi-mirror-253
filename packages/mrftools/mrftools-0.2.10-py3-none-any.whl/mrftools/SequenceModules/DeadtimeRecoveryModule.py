from ..Types import RecoveryType, SequenceUnits, Units
from . import RecoveryModule, Register
import torch

@Register 
class DeadtimeRecoveryModule(RecoveryModule):
    """
    A module representing deadtime recovery in a sequence.

    Args:
        totalDuration (float): The total duration of deadtime recovery in seconds.
        units (SequenceUnits, optional): The units of time. Defaults to None.
    """
    def __init__(self, totalDuration, units=None):
        """
        Initialize a DeadtimeRecoveryModule instance.

        Args:
            totalDuration (float): The total duration of deadtime recovery in seconds.
            units (SequenceUnits, optional): The units of time. Defaults to None.
        """
        RecoveryModule.__init__(self, recoveryType=RecoveryType.DEADTIME, units=units) 
        self.totalDuration = totalDuration   # Seconds

    def __str__(self):
        """
        Return a string representation of the module.

        Returns:
            str: A formatted string representation.
        """
        return RecoveryModule.__str__(self) + " || Total Duration (s): " + f'{self.totalDuration:7.5f}'
    
    def __dict__(self):
        """
        Return a dictionary representation of the module.

        Returns:
            dict: A dictionary containing module information.
        """
        moduleDict  = {
            "type": str(self.__class__.__name__),
            "totalDuration": self.totalDuration,
        }
        return moduleDict
        
    def ConvertUnits(self, targetUnits:SequenceUnits):
        """
        Convert the units of total duration to the target units.

        Args:
            targetUnits (SequenceUnits): The target units for conversion.
        """
        if(self.units != targetUnits):
            self.totalDuration =  Units.Convert(self.totalDuration, self.units.time, targetUnits.time)
            self.units = targetUnits

    def CastToIntegers(self):
        """Cast total duration value to an integer."""
        self.totalDuration = int(self.totalDuration)
    
    def CastToFloats(self):
        """Cast total duration value to a float."""
        self.totalDuration = float(self.totalDuration)

    @staticmethod
    def FromJson(jsonInput):  
        """
        Create a DeadtimeRecoveryModule instance from a JSON input.

        Args:
            jsonInput (dict): The JSON input containing module information.

        Returns:
            DeadtimeRecoveryModule: The created DeadtimeRecoveryModule instance.
        """
        totalDuration = jsonInput.get("totalDuration")
        if totalDuration != None:
            return DeadtimeRecoveryModule(totalDuration)
        else:
            print("DeadtimeRecoveryModule requires totalDuration")
    
    def Simulate(self, dictionaryEntries, numSpins, device=None, inputMx=None, inputMy=None, inputMz=None): 
        """
        Simulate deadtime recovery for a given set of dictionary entries.

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

        numDictionaryEntries = len(dictionaryEntries)
        Mx0 = torch.zeros((1, numSpins, numDictionaryEntries))
        My0 = torch.zeros((1, numSpins, numDictionaryEntries))
        Mz0 = torch.zeros((1, numSpins, numDictionaryEntries))
        Time = torch.zeros((1))

        Mx = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        My = torch.zeros((numSpins, numDictionaryEntries)).to(device)
        Mz = torch.zeros((numSpins, numDictionaryEntries)).to(device)    
        TR = self.totalDuration
            
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
                tr = TR
                At2tr = torch.exp(-1*tr/T2s)
                At1tr = torch.exp(-1*tr/T1s)
                Bt1tr = 1-At1tr

                # Relaxation over prep duration
                Mx = torch.multiply(Mx, At2tr)
                My = torch.multiply(My, At2tr)
                Mz = torch.multiply(Mz, At1tr)+Bt1tr

                # Reading value after TR and before TRE 
                Mx0[0,:,:]=Mx.cpu()
                My0[0,:,:]=My.cpu()
                Mz0[0,:,:]=Mz.cpu()
                Time[0] = self.totalDuration
                del tr, At2tr, At1tr, Bt1tr
        del T1s, T2s, B1s, TR, Mx, My, Mz
        return Time,Mx0,My0,Mz0
