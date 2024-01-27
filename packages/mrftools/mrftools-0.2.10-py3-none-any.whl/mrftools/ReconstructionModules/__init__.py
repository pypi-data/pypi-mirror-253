name = 'mrftools.ReconstructionModules'

RegisteredReconstructionModules = {}

def Register(cls):
    RegisteredReconstructionModules[cls.__name__] = cls
    return cls

from .ReconstructionModule import ReconstructionModule

from .CoilCompressionModule import CoilCompressionModule
from .SVDCompressionModule import SVDCompressionModule
from .NUFFTModule import NUFFTModule
from .IterativeNUFFTModule import IterativeNUFFTModule
from .IFFTModule import IFFTModule
from .CoilCombinationModule import CoilCombinationModule
from .PatternMatchingModule import PatternMatchingModule
from .ScalingModule import ScalingModule
from .IterativeRadialMaskingModule import IterativeRadialMaskingModule