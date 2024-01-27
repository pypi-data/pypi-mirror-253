from ..Types import SequenceModuleType, AcquisitionType, Timepoint, Units, SequenceUnits
from . import SequenceModule
import numpy as np

class AcquisitionModule(SequenceModule):
    """
    A module representing an acquisition/readout block in a sequence.

    Args:
        acquisitionType (AcquisitionType): The type of acquisition.
        timepoints (list, optional): List of timepoints. Defaults to an empty list.
        units (SequenceUnits, optional): The units of the timepoints. Defaults to None.
    """

    def __init__(self, acquisitionType:AcquisitionType, timepoints=[], units=None):
        """
        Initialize an AcquisitionModule instance.

        Args:
            acquisitionType (AcquisitionType): The type of acquisition.
            timepoints (list, optional): List of timepoints. Defaults to an empty list.
            units (SequenceUnits, optional): The units of the timepoints. Defaults to None.
        """
        SequenceModule.__init__(self, moduleType=SequenceModuleType.ACQUISITION, units=units) 
        self.acquisitionType = acquisitionType
        self.timepoints = timepoints 

    def Initialize(self, TRs, TEs, FAs, PHs, IDs):
        """
        Initialize the acquisition module with timepoint values.

        Args:
            TRs (list): List of repetition times.
            TEs (list): List of echo times.
            FAs (list): List of flip angles.
            PHs (list): List of phase values.
            IDs (list): List of IDs.
        """
        self.timepoints = np.empty(len(TRs), dtype=np.dtype([('TR', np.float32), ('TE', np.float32), ('FA', np.float32), ('PH', np.float32), ('ID', np.int16)]))
        if (len(TRs)!=len(TEs)) or (len(TRs)!=len(FAs)) or  (len(TRs)!=len(PHs)) or  (len(TRs)!=len(IDs)):
            print("Sequence Parameter Import Failed: TR/TE/FA/PH/ID files must have identical number of entries")
        else:
            for index in range(len(TRs)):
                self.timepoints[index] = (TRs[index], TEs[index], FAs[index], PHs[index], IDs[index])
    
    def ConvertUnits(self, targetUnits:SequenceUnits):
        """
        Convert the units of timepoints to the target units.

        Args:
            targetUnits (SequenceUnits): The target units for conversion.
        """
        if(self.units != targetUnits):
            scaledTimepoints = np.copy(self.timepoints)
            scaledTimepoints['TR'] = Units.Convert(self.timepoints['TR'], self.units.time, targetUnits.time)
            scaledTimepoints['TE'] = Units.Convert(self.timepoints['TE'], self.units.time, targetUnits.time)
            scaledTimepoints['FA'] = Units.Convert(self.timepoints['FA'], self.units.angle, targetUnits.angle)
            scaledTimepoints['PH'] = Units.Convert(self.timepoints['PH'], self.units.angle, targetUnits.angle)
            self.timepoints = scaledTimepoints
            self.units = targetUnits

    def CastToIntegers(self):
        """Cast timepoint values to integers."""
        scaledTimepoints = self.timepoints.astype(np.dtype([('TR', int), ('TE', int), ('FA', int), ('PH', int), ('ID', int)]))
        self.timepoints = scaledTimepoints
    
    def CastToFloats(self):
        """Cast timepoint values to floats."""
        scaledTimepoints = self.timepoints.astype(Timepoint)
        self.timepoints = scaledTimepoints