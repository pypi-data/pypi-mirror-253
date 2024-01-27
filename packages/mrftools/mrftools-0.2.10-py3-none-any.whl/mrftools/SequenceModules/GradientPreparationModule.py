from ..Types import PreparationType, GradientType
from . import PreparationModule

class GradientPreparationModule(PreparationModule):
    """
    Base class representing a gradient preparation module in a sequence.

    Args:
        gradientType (GradientType): The type of gradient used.
        units (SequenceUnits, optional): The units of the gradient. Defaults to None.
    """
    def __init__(self, gradientType:GradientType, units=None):
        """
        Initialize a GradientPreparationModule instance.

        Args:
            gradientType (GradientType): The type of gradient used.
            units (SequenceUnits, optional): The units of the gradient. Defaults to None.
        """
        PreparationModule.__init__(self, preparationType=PreparationType.GRADIENT, units=units) 
        self.gradientType = gradientType
    def __str__(self):
        """
        Return a string representation of the module.

        Returns:
            str: A formatted string representation.
        """
        return PreparationModule.__str__(self) + " || Gradient Type: " + self.gradientType.name
    