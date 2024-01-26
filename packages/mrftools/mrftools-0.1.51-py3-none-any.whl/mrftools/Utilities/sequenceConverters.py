from mrftools import SequenceParameters
from mrftools.Types import Units, SequenceUnits
from mrftools.Utilities import ScaledRectifiedSinusoid, Perlin, BitReverse
from mrftools.SequenceModules import *
import numpy as np

def LegacyReader(name:str, version:str, filepath:str, inversionTimeSeconds:float=0.020640, delayTimeSeconds:float=2.0000, dephasingRangeDegrees:int=360):
    file = open(filepath, 'r')
    lines = file.read().splitlines()
    timeUnits = Units[lines[0]]
    angleUnits = Units[lines[1]]
    sequenceType = lines[2]
    TRs=[]; TEs=[]; FAs=[]; PHs=[]; IDs=[]
    for lineNumber in np.arange(4, len(lines)):
        vals = lines[lineNumber].split()
        TRs.append(float(vals[0]))
        TEs.append(float(vals[1]))
        FAs.append(float(vals[2]))
        PHs.append(float(vals[3]))
        IDs.append(int(vals[4]))

    file.close()

    if(sequenceType == "FISP"):
        acquisitionModule = FISPAcquisitionModule(dephasingRange=dephasingRangeDegrees, units=SequenceUnits(timeUnits, angleUnits))
        acquisitionModule.Initialize(TRs, TEs, FAs, PHs,IDs)
    elif(sequenceType == "TRUEFISP"):
        acquisitionModule = TRUEFISPAcquisitionModule(units=SequenceUnits(timeUnits, angleUnits))
        acquisitionModule.Initialize(TRs, TEs, FAs, PHs,IDs)        

    # Create sequence parameter definition programmatically
    sequence = SequenceParameters(name, [], version=version)
    sequence.modules.append(InversionModule(totalDuration=inversionTimeSeconds))
    sequence.modules.append(acquisitionModule)
    sequence.modules.append(DeadtimeRecoveryModule(delayTimeSeconds))
    sequence.ConvertUnits(SequenceUnits(time=Units.SECONDS, angle=Units.DEGREES))
    return sequence
    