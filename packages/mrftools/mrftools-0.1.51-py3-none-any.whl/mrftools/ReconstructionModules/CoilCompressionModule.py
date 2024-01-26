from ..Types import ReconstructionModuleIOType, KspaceData
from . import ReconstructionModule, Register
from ..Utilities import dump_tensors
import torch
import gc

def GetTruncationNumberFromDesiredPower(singularValues, desiredSVDPower):
    """
    Get the truncation number based on desired SVD power.

    Args:
        singularValues (torch.Tensor): Singular values from SVD.
        desiredSVDPower (float): Desired cumulative SVD power.

    Returns:
        int: Truncation number.
    """
    singularVectorPowers = singularValues/torch.sum(singularValues)
    totalSVDPower=0; numSVDComponents=0
    for singularVectorPower in singularVectorPowers:
        totalSVDPower += singularVectorPower
        numSVDComponents += 1
        if totalSVDPower > desiredSVDPower:
            break
    return numSVDComponents, totalSVDPower

def GetPowerFromDesiredTruncationNumber(singularValues, desiredTruncationNumber):
    """
    Get the cumulative SVD power from desired truncation number.

    Args:
        singularValues (torch.Tensor): Singular values from SVD.
        desiredTruncationNumber (int): Desired truncation number.

    Returns:
        float: Cumulative SVD power.
    """
    singularVectorPowers = singularValues/torch.sum(singularValues)
    totalSVDPower=torch.sum(singularVectorPowers[0:desiredTruncationNumber])
    return totalSVDPower

def PerformSVDCoilCompression(rawData, desiredSVDPower=0.99, truncationNumberOverride=-1, device=None):
    """
    Perform SVD-based coil compression on raw k-space data.

    Args:
        rawData (torch.Tensor): Raw k-space data of shape [coil, partition, readout, spiral, spiralTimepoint].
        desiredSVDPower (float, optional): Desired cumulative SVD power. Defaults to 0.99.
        truncationNumberOverride (int, optional): Override for truncation number. Defaults to -1.
        device (torch.device, optional): Device for computation. Defaults to None.

    Returns:
        torch.Tensor: Coil-compressed k-space data of shape [coil, partition, readout, spiral, spiralTimepoint].
        int: Actual truncation number used.
        float: Actual cumulative SVD power achieved.
    """
    with torch.no_grad():
        shape = rawData.shape
        linearizedData = rawData.reshape(shape[0], -1).t()
        (u,s,v) = torch.linalg.svd(linearizedData, full_matrices=False)
        vt = v.t()
        if truncationNumberOverride == -1:
            (truncationNumber, totalSVDPower) = GetTruncationNumberFromDesiredPower(s, desiredSVDPower)
        else:
            truncationNumber = truncationNumberOverride
            totalSVDPower = GetPowerFromDesiredTruncationNumber(s, truncationNumber)
        truncationMatrix = vt[:,0:truncationNumber]
        coilCompressed = torch.matmul(linearizedData,truncationMatrix).t()
        coilCompressedResults = coilCompressed.reshape(truncationNumber, shape[1], shape[2], shape[3], shape[4])
        return coilCompressedResults, truncationNumber, totalSVDPower

@Register
class CoilCompressionModule(ReconstructionModule):
    """
    Coil compression module using SVD-based coil compression.

    Args:
        reconstructionParameters (dict): Parameters specific to the reconstruction module.
        inputType (ReconstructionModuleIOType, optional): Input data type. Defaults to ReconstructionModuleIOType.KSPACE.
        outputType (ReconstructionModuleIOType, optional): Output data type. Defaults to ReconstructionModuleIOType.KSPACE.
        svdPower (float, optional): Desired cumulative SVD power. Defaults to 0.9.
        truncationNumberOverride (int, optional): Override for truncation number. Defaults to -1.
        device (torch.device, optional): Device for computation. Defaults to None.
    """
    def __init__(self, reconstructionParameters, inputType:ReconstructionModuleIOType=ReconstructionModuleIOType.KSPACE, outputType:ReconstructionModuleIOType=ReconstructionModuleIOType.KSPACE, svdPower=0.9, truncationNumberOverride=-1, device=None):
        """
        Initialize the CoilCompressionModule.

        Args:
            reconstructionParameters (dict): Parameters specific to the reconstruction module.
            inputType (ReconstructionModuleIOType, optional): Input data type. Defaults to ReconstructionModuleIOType.KSPACE.
            outputType (ReconstructionModuleIOType, optional): Output data type. Defaults to ReconstructionModuleIOType.KSPACE.
            svdPower (float, optional): Desired cumulative SVD power. Defaults to 0.9.
            truncationNumberOverride (int, optional): Override for truncation number. Defaults to -1.
            device (torch.device, optional): Device for computation. Defaults to None.
        """
        ReconstructionModule.__init__(self, reconstructionParameters=reconstructionParameters, inputType=inputType, outputType=outputType) 
        self.svdPower = svdPower
        self.truncationNumberOverride = truncationNumberOverride 
        if(device is None):
            self.device = reconstructionParameters.defaultDevice
        else:
            self.device = device

    def __dict__(self):
        """
        Convert module attributes to a dictionary.

        Returns:
            dict: Dictionary containing module attributes.
        """
        moduleDict  = {
            "type": str(self.__class__.__name__),
            "inputType": str(self.inputType.name),
            "outputType": str(self.outputType.name),
            "svdPower": self.svdPower,
            "truncationNumberOverride": self.truncationNumberOverride
        }
        return moduleDict

    def ProcessKspaceToKspace(self, inputData):
        
        """
        Process k-space data to k-space data using coil compression.

        Args:
            inputData (KspaceData): Input k-space data.

        Returns:
            KspaceData: Processed k-space data.
        """
        with torch.no_grad():
            outputData,_,_ = PerformSVDCoilCompression(inputData, desiredSVDPower=self.svdPower, truncationNumberOverride=self.truncationNumberOverride)
            return KspaceData(outputData)

    @staticmethod
    def FromJson(jsonInput, reconstructionParameters, inputType, outputType):  
        """
        Create an instance of CoilCompressionModule from JSON input.

        Args:
            jsonInput (dict): JSON input containing module details.
            reconstructionParameters (dict): Parameters specific to the reconstruction module.
            inputType (ReconstructionModuleIOType): Input data type.
            outputType (ReconstructionModuleIOType): Output data type.

        Returns:
            CoilCompressionModule: Instance of CoilCompressionModule.
        """
        svdPower = jsonInput.get("svdPower")
        truncationNumberOverride = jsonInput.get("truncationNumberOverride")
        if svdPower != None and truncationNumberOverride != None:
            return CoilCompressionModule(reconstructionParameters, inputType, outputType, svdPower, truncationNumberOverride)
        else:
            print("CoilCombinationModule requires svdPower and truncationNumberOverride")
        