from __future__ import annotations
import torch
import json as json
from . import SimulationParameters
from .Types import Units, SequenceUnits
from .ReconstructionModules import ReconstructionModule
from .Utilities import dump_tensors
from importlib.metadata import version  
import time

class ReconstructionParameters:
    """
    A class to manage reconstruction parameters for MRI simulations.
    """

    def __init__(self, name:str, simulation:SimulationParameters, version="dev", outputMatrixSize=[-1,-1,-1], modules=[], defaultDevice=torch.device("cpu")):
        """
        Initialize a ReconstructionParameters object.

        Parameters
        ----------
        name : str
            Name of the reconstruction.
        simulation : SimulationParameters
            Simulation parameters associated with the reconstruction.
        version : str, optional
            Version of the reconstruction, by default "dev".
        outputMatrixSize : list[int], optional
            Output matrix size for reconstruction, by default [-1, -1, -1].
        modules : list[ReconstructionModule], optional
            List of reconstruction modules, by default an empty list.
        defaultDevice : torch.device, optional
            Default device for computation, by default torch.device("cpu").
        """
        self.name = name
        self.version = version
        self.simulation = simulation
        self.outputMatrixSize = outputMatrixSize
        self.modules = modules 
        self.defaultDevice = defaultDevice

    def __str__(self):
        """
        Returns a human-readable string representation of the reconstruction.

        Returns
        -------
        str
            A string representation of the reconstruction.
        """
        moduleDescriptions = ""
        for module in self.modules:
            moduleDescriptions = moduleDescriptions + str(module) + "\n------------------\n"
        return "Reconstruction: " + self.name + "\nModules:\n------------------\n" + moduleDescriptions
    
    def __dict__(self):
        """
        Returns a dictionary representation of the ReconstructionParameters object for the purposes of JSON serialization.

        Returns
        -------
        dict
            A dictionary representation of the object.
        """
        mrftools_version = version("mrftools")
        reconstructionDict  = {
            "name": self.name,
            "version": self.version,
            "outputMatrixSize": self.outputMatrixSize,
            "defaultDevice": self.defaultDevice.type,
            "modules": [],
            "simulation": self.simulation.__dict__().get("simulation")
        }
        for module in self.modules:
            reconstructionDict.get("modules").append(module.__dict__())
        reconstructionParametersDict = {
            "mrftools_version":mrftools_version,
            "reconstruction":reconstructionDict
        }
        return reconstructionParametersDict
    
    ## Cast to integers during export is NOT a lossless process, so that simulations run on the exported data match scanner execution
    def ExportToJson(self, baseFilepath=""):
        """
        Exports the reconstruction to a JSON file.

        Parameters
        ----------
        baseFilepath : str, optional
            Base filepath for the JSON file, by default an empty string.
        """
        reconstructionFilename = baseFilepath+self.name+"_"+self.version+".reconstruction"
        with open(reconstructionFilename, 'w') as outfile:
            json.dump(self.__dict__(), outfile, indent=2)
    
    def Run(self, input):
        """
        Runs the reconstruction on the given input data.

        Parameters
        ----------
        input : torch.Tensor
            Input data for the reconstruction.

        Returns
        -------
        torch.Tensor
            Output of the reconstruction process.
        """
        with torch.no_grad():
            current = input
            for module in self.modules:
                startTime = time.time()
                current = module.Process(current)
                print(module.__class__.__name__, f'({time.time() - startTime}sec)')
                print(current.data.shape)
            return current

    @staticmethod
    def FromJson(inputJson):
        """
        Creates a ReconstructionParameters object from a JSON string input.

        Parameters
        ----------
        inputJson : dict
            JSON input containing reconstruction information.

        Returns
        -------
        ReconstructionParameters
            A new ReconstructionParameters object created from the input JSON.
        """
        mrftoolsVersion = inputJson.get("mrftools_version")
        reconstructionJson = inputJson.get("reconstruction")
        reconstructionName = reconstructionJson.get("name")
        simulationJson = reconstructionJson.get("simulation")
        simulation = SimulationParameters.FromJson(simulationJson)
        reconstructionVersion = reconstructionJson.get("version")
        outputMatrixSize = reconstructionJson.get("outputMatrixSize")
        defaultDevice = reconstructionJson.get("defaultDevice")
        reconstructionParameters = ReconstructionParameters(reconstructionName, simulation, reconstructionVersion, outputMatrixSize, [], torch.device(defaultDevice))
        modulesJson = reconstructionJson.get("modules")
        for moduleJson in modulesJson:
            reconstructionParameters.modules.append(ReconstructionModule.FromJson(moduleJson, reconstructionParameters))
        return reconstructionParameters

    @staticmethod
    def FromFile(path):
        """
        Creates a ReconstructionParameters object from a JSON file.

        Parameters
        ----------
        path : str
            Path to the JSON file.

        Returns
        -------
        ReconstructionParameters
            A new ReconstructionParameters object created from the JSON file.
        """
        with open(path) as inputFile:
            inputJson = json.load(inputFile)
            return ReconstructionParameters.FromJson(inputJson)

