from ..Types import PreparationType, RFType
from . import PreparationModule

class RFPreparationModule(PreparationModule):
    """
    Base class representing an RF preparation module in a sequence.

    Args:
        rfType (RFType): The type of RF preparation.
        units (SequenceUnits, optional): The units of the module. Defaults to None.
    """
    def __init__(self, rfType:RFType, units=None):
        """
        Initialize an RFPreparationModule instance.

        Args:
            rfType (RFType): The type of RF preparation.
            units (SequenceUnits, optional): The units of the module. Defaults to None.
        """
        PreparationModule.__init__(self, preparationType=PreparationType.RF, units=units) 
        self.rfType = rfType
    def __str__(self):
        """
        Generate a string representation of the module.

        Returns:
            str: The string representation of the module.
        """
        return PreparationModule.__str__(self) + " || RF Type: " + self.rfType.name
    