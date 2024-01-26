from ..Types import SequenceModuleType, Units, SequenceUnits
from . import RegisteredSequenceModules

class SequenceModule:
    """
    Base class representing a sequence module.

    Args:
        moduleType (SequenceModuleType): The type of the module.
        units (SequenceUnits, optional): The units of the module. Defaults to None.
    """
    def __init__(self, moduleType:SequenceModuleType, units=None):
        """
        Initialize a SequenceModule instance.

        Args:
            moduleType (SequenceModuleType): The type of the module.
            units (SequenceUnits, optional): The units of the module. Defaults to None.
        """
        self.moduleType = moduleType
        if(units != None):
            self.units = units
        else:
            self.units = SequenceUnits(Units.SECONDS, Units.DEGREES)

    def __str__(self):
        """
        Generate a string representation of the module.

        Returns:
            str: The string representation of the module.
        """
        return "Module Type: " + self.moduleType.name
    
    @staticmethod
    def FromJson(jsonInput, units):
        """
        Create an instance of a specific module from JSON input.

        Args:
            jsonInput (dict): The JSON input data.
            units (SequenceUnits): The units for the module.

        Returns:
            SequenceModule: An instance of the specific module.
        """
        moduleClass = RegisteredSequenceModules[jsonInput.get("type")]
        module = moduleClass.FromJson(jsonInput)
        module.units = units
        return module
