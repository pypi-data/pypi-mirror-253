from ..Types import SequenceModuleType, RecoveryType, RFType
from . import SequenceModule

class RecoveryModule(SequenceModule):
    """
    Base class representing a recovery module in a sequence.

    Args:
        recoveryType (RecoveryType): The type of recovery.
        units (SequenceUnits, optional): The units of the module. Defaults to None.
    """
    def __init__(self, recoveryType:RecoveryType, units=None):
        """
        Initialize a RecoveryModule instance.

        Args:
            recoveryType (RecoveryType): The type of recovery.
            units (SequenceUnits, optional): The units of the module. Defaults to None.
        """
        SequenceModule.__init__(self, moduleType=SequenceModuleType.RECOVERY, units=units) 
        self.recoveryType = recoveryType
    def __str__(self):
        """
        Generate a string representation of the module.

        Returns:
            str: The string representation of the module.
        """
        return SequenceModule.__str__(self) + " || Recovery Type: " + self.recoveryType.name
