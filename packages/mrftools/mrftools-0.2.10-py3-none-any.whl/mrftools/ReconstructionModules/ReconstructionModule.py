from ..Types import ReconstructionModuleIOType, DataStruct
from . import RegisteredReconstructionModules

class ReconstructionModule:
    """
    Base class for reconstruction modules.
    
    Args:
        reconstructionParameters (dict): Parameters specific to the reconstruction module.
        inputType (ReconstructionModuleIOType): Input data type for the module.
        outputType (ReconstructionModuleIOType): Output data type for the module.
    """

    def __init__(self, reconstructionParameters, inputType:ReconstructionModuleIOType, outputType: ReconstructionModuleIOType):
        self.reconstructionParameters = reconstructionParameters
        self.inputType = inputType
        self.outputType = outputType

    def __str__(self):
        """
        Get a string representation of the reconstruction module.

        Returns:
            str: String representation of the module.
        """
        return "Input: " + self.inputType.name + " | Output: " + self.outputType.name
    
    def Process(self, input:DataStruct):
        """
        Process input data using the reconstruction module.

        Args:
            input (DataStruct): Input data to be processed.

        Returns:
            Any: Processed output data.
        """
        if(input.dataType == self.inputType):
            if(self.inputType == ReconstructionModuleIOType.KSPACE and self.outputType == ReconstructionModuleIOType.KSPACE):
                return self.ProcessKspaceToKspace(input.data)
            elif(self.inputType == ReconstructionModuleIOType.KSPACE and self.outputType == ReconstructionModuleIOType.IMAGE):
                return self.ProcessKspaceToImage(input.data)
            elif(self.inputType == ReconstructionModuleIOType.IMAGE and self.outputType == ReconstructionModuleIOType.IMAGE):
                return self.ProcessImageToImage(input.data)
            elif(self.inputType == ReconstructionModuleIOType.IMAGE and self.outputType == ReconstructionModuleIOType.MAP):
                return self.ProcessImageToMap(input.data)
            elif(self.inputType == ReconstructionModuleIOType.MAP and self.outputType == ReconstructionModuleIOType.MAP):
                return self.ProcessMapToMap(input.data)
            else:
                return None
        else:
            return None

    def ProcessKspaceToKspace(self, inputData):
        """
        Process k-space data to k-space data.

        Args:
            inputData: Input k-space data.

        Returns:
            Any: Processed k-space data.
        """
        return None
    
    def ProcessKspaceToImage(self, inputData):
        """
        Process k-space data to image data.

        Args:
            inputData: Input k-space data.

        Returns:
            Any: Processed image data.
        """
        return None
    
    def ProcessImageToImage(self, inputData):
        """
        Process image data to image data.

        Args:
            inputData: Input image data.

        Returns:
            Any: Processed image data.
        """
        return None
    
    def ProcessImageToMap(self, inputData):
        """
        Process image data to map data.

        Args:
            inputData: Input image data.

        Returns:
            Any: Processed map data.
        """
        return None
    
    def ProcessMapToMap(self, inputData):
        """
        Process map data to map data.

        Args:
            inputData: Input map data.

        Returns:
            Any: Processed map data.
        """
        return None
    
    @staticmethod
    def FromJson(jsonInput, reconstructionParameters):
        """
        Create a reconstruction module instance from JSON input.

        Args:
            jsonInput (dict): JSON input containing module details.
            reconstructionParameters (dict): Parameters specific to the reconstruction module.

        Returns:
            ReconstructionModule: Instance of the reconstructed module.
        """
        moduleClass = RegisteredReconstructionModules[jsonInput.get("type")]
        inputType = ReconstructionModuleIOType[jsonInput.get("inputType")]
        outputType = ReconstructionModuleIOType[jsonInput.get("outputType")]
        module = moduleClass.FromJson(jsonInput, reconstructionParameters, inputType, outputType)
        return module
