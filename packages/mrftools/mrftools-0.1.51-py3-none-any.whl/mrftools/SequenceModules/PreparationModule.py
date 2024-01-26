from ..Types import SequenceModuleType, PreparationType
from . import SequenceModule

class PreparationModule(SequenceModule):
    """
    Base class representing a preparation module in a sequence.

    Args:
        preparationType (PreparationType): The type of preparation.
        units (SequenceUnits, optional): The units of the module. Defaults to None.
    """
    def __init__(self, preparationType:PreparationType, units=None):
        """
        Initialize a PreparationModule instance.

        Args:
            preparationType (PreparationType): The type of preparation.
            units (SequenceUnits, optional): The units of the module. Defaults to None.
        """
        SequenceModule.__init__(self, moduleType=SequenceModuleType.PREPARATION, units=units) 
        self.preparationType = preparationType
    def __str__(self):
        """
        Generate a string representation of the module.

        Returns:
            str: The string representation of the module.
        """
        return SequenceModule.__str__(self) + " || Preparation Type: " + self.preparationType.name
