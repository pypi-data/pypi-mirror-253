from __future__ import annotations
import torch
import json as json
from .Types import Units, SequenceUnits
from .SequenceModules import SequenceModule
from . import TrajectoryParameters
from importlib.metadata import version  

class SequenceParameters:
    """
    A class to manage sequence parameters for MRI simulations.
    """

    def __init__(self, name:str, modules=[], trajectory:TrajectoryParameters=None, version="dev", sequenceUnits=SequenceUnits(Units.SECONDS,Units.DEGREES)):
        """
        Initialize a SequenceParameters object.

        Parameters:
            name (str): Name of the sequence.
            modules (list[SequenceModule], optional): List of sequence modules, by default an empty list.
            version (str, optional): Version of the sequence, by default "dev".
            sequenceUnits (SequenceUnits, optional): Units of time and angle for the sequence, by default SequenceUnits(Units.SECONDS,Units.DEGREES).
        """
        self.name = name
        self.modules = modules 
        self.trajectory = trajectory
        self.version = version
        self.units = sequenceUnits

    def __str__(self):
        """
        Returns a human-readable string representation of the sequence.

        Returns
        -------
        str
            A string representation of the sequence.
        """
        moduleDescriptions = ""
        for module in self.modules:
            moduleDescriptions = moduleDescriptions + str(module) + "\n------------------\n"
        return "Sequence: " + self.name + "\nModules:\n------------------\n" + moduleDescriptions
    
    def __dict__(self):
        """
        Returns a dictionary representation of the SequenceParameters object for the purposes of JSON serialization.

        Returns
        -------
        dict
            A dictionary representation of the object.
        """
        mrftools_version = version("mrftools")
        sequenceDict  = {
            "name": self.name,
            "version": self.version,
            "units" : self.units.__dict__(),
            "modules": [], 
        }
        if(self.trajectory):
            sequenceDict["trajectory"] =  self.trajectory.__dict__().get("trajectory")

        for module in self.modules:
            sequenceDict.get("modules").append(module.__dict__())
            
        sequenceParametersDict = {
            "mrftools_version":mrftools_version,
            "sequence":sequenceDict
        }
        return sequenceParametersDict

    def ConvertUnits(self, newUnits):
        """
        Converts the sequence units to new specified units.

        Parameters
        ----------
        newUnits : SequenceUnits
            New units of time and angle for the sequence.
        """
        if (self.units.time != newUnits.time) or (self.units.angle != newUnits.angle):
            for module in self.modules:
                module.ConvertUnits(newUnits)
            self.units = newUnits

    def CastToIntegers(self):
        """
        Casts sequence module data to integers.
        """
        for module in self.modules:
            module.CastToIntegers() 

    def CastToFloats(self):
        """
        Casts sequence module data to floats.
        """
        for module in self.modules:
            module.CastToFloats() 
    
    ## Cast to integers during export is NOT a lossless process, so that simulations run on the exported data match scanner execution
    def ExportToJson(self, baseFilepath="", exportUnits=SequenceUnits(Units.MICROSECONDS, Units.CENTIDEGREES), castToIntegers=True):
        """
        Exports the sequence to a JSON file.

        Parameters
        ----------
        baseFilepath : str, optional
            Base filepath for the JSON file, by default an empty string.
        exportUnits : SequenceUnits, optional
            Units for exporting the sequence, by default SequenceUnits(Units.MICROSECONDS, Units.CENTIDEGREES).
        castToIntegers : bool, optional
            Cast module data to integers if True, by default True.
        """
        originalUnits = self.units
        self.ConvertUnits(exportUnits)
        if castToIntegers:
            self.CastToIntegers()
        sequenceFilename = baseFilepath+self.name+"_"+self.version+".sequence"
        with open(sequenceFilename, 'w') as outfile:
            json.dump(self.__dict__(), outfile, indent=2)
        if castToIntegers:
            self.CastToFloats()
        self.ConvertUnits(originalUnits)
    
    def Simulate(self, dictionaryEntries, numSpins, device=None):
        """
        Simulates the sequence given dictionary entries and number of spins.

        Parameters
        ----------
        dictionaryEntries : torch.Tensor
            Dictionary entries for simulation.
        numSpins : int
            Number of spins for simulation.
        device : torch.device, optional
            Device for computation, by default None.

        Returns
        -------
        tuple
            A tuple containing simulation results.
        """
        from .SequenceModules.AcquisitionModule import AcquisitionModule
        if self.units.time != Units.SECONDS or self.units.angle != Units.DEGREES:
            print("Sequence Units are not the required Seconds/Degrees. Converting before simulation. ")
            self.ConvertUnits(SequenceUnits(Units.SECONDS, Units.DEGREES))
            
        Time = torch.zeros([1]); 
        Mx0 = torch.zeros([1,numSpins, len(dictionaryEntries)]); ReadoutMx0 = torch.zeros([1,numSpins, len(dictionaryEntries)]); 
        My0 = torch.zeros([1,numSpins, len(dictionaryEntries)]); ReadoutMy0 = torch.zeros([1,numSpins, len(dictionaryEntries)]); 
        Mz0 = torch.ones([1,numSpins, len(dictionaryEntries)]);  ReadoutMz0 = torch.ones([1,numSpins, len(dictionaryEntries)])

        for module in self.modules:
            resultTime, resultMx0, resultMy0, resultMz0 = module.Simulate(dictionaryEntries, numSpins, device=device, inputMx=Mx0[-1,:,:], inputMy=My0[-1,:,:], inputMz=Mz0[-1,:,:])
            Time = torch.cat((Time, resultTime+Time[-1])); Mx0 = torch.cat((Mx0, resultMx0)); My0 = torch.cat((My0, resultMy0)); Mz0 = torch.cat((Mz0, resultMz0)); 
            
            if(issubclass(module.__class__, AcquisitionModule)):
                ReadoutMx0 = torch.cat((ReadoutMx0, resultMx0))
                ReadoutMy0 = torch.cat((ReadoutMy0, resultMy0))
                ReadoutMz0 = torch.cat((ReadoutMz0, resultMz0))
        return Time, (Mx0, My0, Mz0), (ReadoutMx0, ReadoutMy0, ReadoutMz0)

    @staticmethod
    def FromJson(inputJson):
        """
        Creates a SequenceParameters object from a JSON input string.

        Parameters
        ----------
        inputJson : dict
            JSON input containing sequence information.

        Returns
        -------
        SequenceParameters
            A new SequenceParameters object created from the input JSON.
        """
        mrftoolsVersion = inputJson.get("mrftools_version")
        
        if(mrftoolsVersion != None):
            sequenceJson = inputJson.get("sequence")
        else: 
            sequenceJson = inputJson
        sequenceName = sequenceJson.get("name")
        sequenceVersion = sequenceJson.get("version")
        unitsJson = sequenceJson.get("units")
        sequenceUnits = SequenceUnits.FromJson(unitsJson)

        sequenceTrajectory = None
        trajectoryJson = sequenceJson.get("trajectory")
        if(trajectoryJson):
            sequenceTrajectory = TrajectoryParameters.FromJson(trajectoryJson)

        modulesJson = sequenceJson.get("modules")
        sequenceModules = []
        for moduleJson in modulesJson:
            sequenceModules.append(SequenceModule.FromJson(moduleJson, sequenceUnits))

        return SequenceParameters(sequenceName,sequenceModules, sequenceTrajectory, sequenceVersion, sequenceUnits)
    
    @staticmethod
    def FromFile(path):
        """
        Creates a SequenceParameters object from a JSON file.

        Parameters
        ----------
        path : str
            Path to the JSON file.

        Returns
        -------
        SequenceParameters
            A new SequenceParameters object created from the JSON file.
        """
        with open(path) as inputFile:
            inputJson = json.load(inputFile)
            return SequenceParameters.FromJson(inputJson)