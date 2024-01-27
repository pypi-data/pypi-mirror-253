from ..Types import ReconstructionModuleIOType, KspaceData
from . import ReconstructionModule, Register
import torch

# Raw Data should have shape [coil, partitions, readouts, spirals, spiralTimepoints]
def ApplySVDCompression(rawdata, simulation, device=None):
    """
    Apply SVD compression to raw k-space data.

    Args:
        rawdata (torch.Tensor): Raw k-space data of shape [coil, partitions, readouts, spirals, spiralTimepoints].
        simulation (SimulationParameters): The simulation parameters.
        device (torch.device, optional): The device on which to perform the operation. Defaults to None.

    Returns:
        torch.Tensor: SVD compressed k-space data.
    """
    with torch.no_grad():
        sizes = rawdata.shape
        numCoils=sizes[0]; numPartitions=sizes[1]; numReadoutPoints=sizes[2]; numSpirals=sizes[3]; numTimepointsPerSpiralArm=sizes[4]
        numSVDComponents = simulation.truncationMatrix.shape[1]
        svdData = torch.zeros((numSVDComponents, numCoils, numPartitions, numReadoutPoints, numSpirals), dtype=torch.complex64)
        for spiral in torch.arange(0,numSpirals):
            truncationMatrix = torch.zeros((numTimepointsPerSpiralArm, numSVDComponents), dtype=torch.complex64).to(device)
            for spiralTimepoint in torch.arange(0,numTimepointsPerSpiralArm):
                realTimepoint = numSpirals*spiralTimepoint + spiral
                truncationMatrix[spiralTimepoint, :] = torch.tensor(simulation.truncationMatrix[realTimepoint, :]).to(device)
            raw = rawdata[:,:,:,spiral, :].to(torch.complex64).to(device)
            result = torch.matmul(raw, truncationMatrix)
            svdData[:,:, :, :, spiral] = torch.moveaxis(result.cpu(), -1, 0)
            del raw, truncationMatrix, result
        return torch.moveaxis(svdData, 0, -1)

@Register
class SVDCompressionModule(ReconstructionModule):
    """
    A module for applying SVD compression to k-space data.

    Args:
        reconstructionParameters (ReconstructionParameters): The reconstruction parameters.
        inputType (ReconstructionModuleIOType, optional): The input data type (k-space). Defaults to ReconstructionModuleIOType.KSPACE.
        outputType (ReconstructionModuleIOType, optional): The output data type (k-space). Defaults to ReconstructionModuleIOType.KSPACE.
        device (torch.device, optional): The device on which to perform the operation. Defaults to None.
    """
    def __init__(self, reconstructionParameters, inputType:ReconstructionModuleIOType=ReconstructionModuleIOType.KSPACE, outputType:ReconstructionModuleIOType=ReconstructionModuleIOType.KSPACE, device=None):
        """
        Initialize an SVDCompressionModule instance.

        Args:
            reconstructionParameters (ReconstructionParameters): The reconstruction parameters.
            inputType (ReconstructionModuleIOType, optional): The input data type (k-space). Defaults to ReconstructionModuleIOType.KSPACE.
            outputType (ReconstructionModuleIOType, optional): The output data type (k-space). Defaults to ReconstructionModuleIOType.KSPACE.
            device (torch.device, optional): The device on which to perform the operation. Defaults to None.
        """
        ReconstructionModule.__init__(self, reconstructionParameters=reconstructionParameters, inputType=inputType, outputType=outputType) 
        if(device is None):
            self.device = reconstructionParameters.defaultDevice
        else:
            self.device = device
            
    def __dict__(self):
        """
        Returns a dictionary representation of the module.

        Returns:
            dict: A dictionary containing module information.
        """
        moduleDict  = {
            "type": str(self.__class__.__name__),
            "inputType": str(self.inputType.name),
            "outputType": str(self.outputType.name),
            "device": self.device.type
        }
        return moduleDict

    def ProcessKspaceToKspace(self, inputData):
        """
        Apply SVD compression to k-space data.

        Args:
            inputData (KspaceData): Input k-space data.

        Returns:
            KspaceData: SVD compressed k-space data.
        """
        with torch.no_grad():
            return KspaceData(ApplySVDCompression(inputData, self.reconstructionParameters.simulation, self.device))

    @staticmethod
    def FromJson(jsonInput, reconstructionParameters, inputType, outputType):  
        """
        Create an SVDCompressionModule from a JSON input.

        Args:
            jsonInput (dict): The JSON input containing module configuration.
            reconstructionParameters (ReconstructionParameters): The reconstruction parameters.
            inputType (ReconstructionModuleIOType): The input data type (k-space).
            outputType (ReconstructionModuleIOType): The output data type (k-space).

        Returns:
            SVDCompressionModule: An instance of the SVDCompressionModule class.
        """
        device = jsonInput.get("device")
        if device != None:
            return SVDCompressionModule(reconstructionParameters, inputType, outputType, torch.device(device))
        else:
            print("SVDCompressionModule requires device")