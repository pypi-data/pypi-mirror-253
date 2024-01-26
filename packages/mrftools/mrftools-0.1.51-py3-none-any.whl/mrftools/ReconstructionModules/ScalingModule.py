from ..Types import ReconstructionModuleIOType, KspaceData, ImageData
from . import ReconstructionModule, Register
import numpy as np


@Register
class ScalingModule(ReconstructionModule):
    """
    A module for scaling k-space data or image data by a specified factor.

    Args:
        reconstructionParameters (ReconstructionParameters): The reconstruction parameters.
        inputType (ReconstructionModuleIOType): The input data type (k-space or image).
        outputType (ReconstructionModuleIOType): The output data type (k-space or image).
        scalingFactor (float, optional): The scaling factor to apply. Defaults to 1.
        device (torch.device, optional): The device on which to perform the operation. Defaults to None.
    """
    def __init__(self, reconstructionParameters, inputType:ReconstructionModuleIOType, outputType:ReconstructionModuleIOType, scalingFactor=1, device=None):
        """
        Initialize a ScalingModule instance.

        Args:
            reconstructionParameters (ReconstructionParameters): The reconstruction parameters.
            inputType (ReconstructionModuleIOType): The input data type (k-space or image).
            outputType (ReconstructionModuleIOType): The output data type (k-space or image).
            scalingFactor (float, optional): The scaling factor to apply. Defaults to 1.
            device (torch.device, optional): The device on which to perform the operation. Defaults to None.
        """
        ReconstructionModule.__init__(self, reconstructionParameters=reconstructionParameters, inputType=inputType, outputType=outputType) 
        self.scalingFactor = scalingFactor
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
            "scalingFactor": self.scalingFactor
        }
        return moduleDict

    def DoScaling(self, inputData, scalingFactor):
        """
        Apply scaling to the input data.

        Args:
            inputData (torch.Tensor): The input data to be scaled.
            scalingFactor (float): The scaling factor to apply.

        Returns:
            torch.Tensor: Scaled output data.
        """
        return inputData * scalingFactor

    def ProcessKspaceToKspace(self, inputData):
        """
        Apply scaling to k-space data.

        Args:
            inputData (KspaceData): Input k-space data.

        Returns:
            KspaceData: Scaled k-space data.
        """
        return KspaceData(self.DoScaling(inputData, self.scalingFactor))

    def ProcessImageToImage(self, inputData):
        """
        Apply scaling to image data.

        Args:
            inputData (ImageData): Input image data.

        Returns:
            ImageData: Scaled image data.
        """
        return ImageData(self.DoScaling(inputData, self.scalingFactor))

    @staticmethod
    def FromJson(jsonInput, reconstructionParameters, inputType, outputType):  
        """
        Create a ScalingModule from a JSON input.

        Args:
            jsonInput (dict): The JSON input containing module configuration.
            reconstructionParameters (ReconstructionParameters): The reconstruction parameters.
            inputType (ReconstructionModuleIOType): The input data type (k-space or image).
            outputType (ReconstructionModuleIOType): The output data type (k-space or image).

        Returns:
            ScalingModule: An instance of the ScalingModule class.
        """
        scalingFactor = jsonInput.get("scalingFactor")
        if scalingFactor != None:
            return ScalingModule(reconstructionParameters, inputType, outputType, scalingFactor)
        else:
            print("CoilCombinationModule requires scalingFactor")