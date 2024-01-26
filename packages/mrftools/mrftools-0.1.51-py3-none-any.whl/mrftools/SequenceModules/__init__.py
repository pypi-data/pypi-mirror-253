name = 'mrftools.SequenceModules'

RegisteredSequenceModules = {}

def Register(cls):
    RegisteredSequenceModules[cls.__name__] = cls
    return cls

from .SequenceModule import SequenceModule

from .AcquisitionModule import AcquisitionModule
from .PreparationModule import PreparationModule
from .RecoveryModule import RecoveryModule

from .GradientPreparationModule import GradientPreparationModule
from .RFPreparationModule import RFPreparationModule

from .FISPAcquisitionModule import FISPAcquisitionModule
from .TRUEFISPAcquisitionModule import TRUEFISPAcquisitionModule

from .InversionModule import InversionModule
from .T2PreparationModule import T2PreparationModule
from .SpoilerModule import SpoilerModule

from .DeadtimeRecoveryModule import DeadtimeRecoveryModule
