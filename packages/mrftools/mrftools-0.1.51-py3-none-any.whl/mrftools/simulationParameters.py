import numpy as np
import h5py
from matplotlib import pyplot as plt
import torch
from tqdm import tqdm
from . import DictionaryParameters, SequenceParameters
from importlib.metadata import version  
import json as json

class SimulationParameters:
    """
    A class to represent simulation parameters and methods.
    """

    def __init__(self,sequenceParameters, dictionaryParameters, name="", version="dev", numSpins=1, times=[], timeDomainResults=[], results=[], truncationMatrix=[], truncatedResults=[], singularValues=[]):
        """
        Initialize SimulationParameters.

        Args:
            sequenceParameters (SequenceParameters): The sequence parameters.
            dictionaryParameters (DictionaryParameters): The dictionary parameters.
            name (str, optional): Name of the simulation. If not provided, a default name will be generated.
            version (str, optional): Version of the simulation.
            numSpins (int, optional): Number of spins.
            times (list, optional): List of simulation times.
            timeDomainResults (list, optional): Results in the time domain.
            results (list, optional): Simulation results.
            truncationMatrix (list, optional): Truncation matrix.
            truncatedResults (list, optional): Truncated simulation results.
            singularValues (list, optional): Singular values of the simulation.
        """
        self.sequenceParameters = sequenceParameters
        self.dictionaryParameters = dictionaryParameters
        self.numSpins = numSpins
        self.times = times
        self.timeDomainResults = timeDomainResults
        self.results = results
        self.truncationMatrix = truncationMatrix
        self.truncatedResults = truncatedResults
        self.singularValues = singularValues
        if not name:
            self.name = sequenceParameters.name + "_" + dictionaryParameters.name + "_" + str(numSpins)
        else:
            self.name = name
        self.version = version
        #print("Simulation Parameter set '"+ self.name + "' initialized (Sequence: '" + self.sequenceParameters.name + "',  Dictionary: '" + self.dictionaryParameters.name + "') with " + str(self.numSpins) + " spins")
    
    def __dict__(self):
        """
        Returns a dictionary representation of the SimulationParameter object for the purposes of JSON serialization.

        Returns:
            dict: A dictionary representation of the object.
        """
        mrftools_version = version("mrftools")
        sequenceDict = self.sequenceParameters.__dict__().get("sequence")
        dictionaryDict = self.dictionaryParameters.__dict__().get("dictionary")
        truncationMatrixDict = {
            "real": self.truncationMatrix.real.tolist(), 
            "imag": self.truncationMatrix.imag.tolist()
        }
        truncatedResultsDict = {
            "real": self.truncatedResults.real.tolist(), 
            "imag": self.truncatedResults.imag.tolist()
        }
        singularValuesDict = {
            "real": self.singularValues.real.tolist(), 
            "imag": self.singularValues.imag.tolist()
        }
        simulationDict  = {
            "name": self.name,
            "version": self.version,
            "sequence": sequenceDict,
            "dictionary": dictionaryDict,
            "numSpins": self.numSpins, 
            "truncationMatrix": truncationMatrixDict, 
            "truncatedResults": truncatedResultsDict, 
            "singularValues": singularValuesDict
        }
        simulationParametersDict = {
            "mrftools_version": mrftools_version,
            "simulation": simulationDict
        }
        return simulationParametersDict

    def ExportToJson(self, baseFilepath=""):
        """
        Export simulation parameters to a JSON file.

        Args:
            baseFilepath (str, optional): Base filepath for the JSON file.

        Returns:
            None
        """
        simulationFilename = baseFilepath+self.name+"_"+self.version+".simulation"
        with open(simulationFilename, 'w') as outfile:
            json.dump(self.__dict__(), outfile, indent=2)

    @staticmethod
    def FromJson(inputJson):
        """
        Create a SimulationParameters instance from a JSON string input.

        Args:
            inputJson (dict): JSON data containing simulation parameters.

        Returns:
            SimulationParameters: The created SimulationParameters instance.
        """
        mrftoolsVersion = inputJson.get("mrftools_version")
        if(mrftoolsVersion != None):
            #print("Input file mrttools Version:", mrftoolsVersion)
            simulationJson = inputJson.get("simulation")
        else:
            simulationJson = inputJson
        name = simulationJson.get("name")
        version = simulationJson.get("version")
        sequenceJson = simulationJson.get("sequence")
        sequenceParameters = SequenceParameters.FromJson(sequenceJson)
        dictionaryJson = simulationJson.get("dictionary")
        dictionaryParameters = DictionaryParameters.FromJson(dictionaryJson)
        numSpins = simulationJson.get("numSpins")
        truncationMatrixJson = simulationJson.get("truncationMatrix")
        truncationMatrix = np.array(truncationMatrixJson.get("real")) + 1j * np.array(truncationMatrixJson.get("imag"))
        truncatedResultsJson = simulationJson.get("truncatedResults")
        truncatedResults = np.array(truncatedResultsJson.get("real")) + 1j * np.array(truncatedResultsJson.get("imag"))
        singularValuesJson = simulationJson.get("singularValues")
        singularValues = np.array(singularValuesJson.get("real")) + 1j * np.array(singularValuesJson.get("imag"))
        if(name != None and sequenceJson != None and dictionaryJson != None):
            return SimulationParameters(sequenceParameters, dictionaryParameters, name, version, numSpins, None, None, None, truncationMatrix, truncatedResults, singularValues)
        else:
            print("SimulationParameters requires name, sequence, and dictionary")

    @staticmethod
    def FromFile(path):
        """
        Create a SimulationParameters instance from a JSON file.

        Args:
            path (str): Path to the JSON file.

        Returns:
            SimulationParameters: The created SimulationParameters instance.
        """
        with open(path) as inputFile:
            inputJson = json.load(inputFile)
            return SimulationParameters.FromJson(inputJson)
        
    def Execute(self, numBatches=1, device=None):
        """
        Execute the simulation.

        Args:
            numBatches (int, optional): Number of batches.
            device: (str, optional): Device for execution.

        Returns:
            numpy.ndarray: Simulation results.
        """
        if(device==None):
            if torch.cuda.is_available():
                device = torch.device("cuda")
            else:
                device = torch.device("cpu")
        dictEntriesPerBatch = int(len(self.dictionaryParameters.entries)/numBatches)
        print("Simulating " + str(numBatches) + " batch(s) of ~" + str(dictEntriesPerBatch) + " dictionary entries")
        singleResult = self.sequenceParameters.Simulate(self.dictionaryParameters.entries[0], 1)
        self.numTimepoints = np.shape(singleResult[1][0])[0]
        self.numReadoutPoints = np.shape(singleResult[2][0])[0]
        Mxy = np.zeros((self.numTimepoints, len(self.dictionaryParameters.entries)), np.complex128)
        ReadoutMxy = np.zeros((self.numReadoutPoints, len(self.dictionaryParameters.entries)), np.complex128)
        with tqdm(total=numBatches) as pbar:
            for i in range(numBatches):
                firstDictEntry = i*dictEntriesPerBatch
                if i == (numBatches-1):
                    lastDictEntry = len(self.dictionaryParameters.entries)
                else:
                    lastDictEntry = firstDictEntry+dictEntriesPerBatch
                batchDictionaryEntries = self.dictionaryParameters.entries[firstDictEntry:lastDictEntry]
                allResults = self.sequenceParameters.Simulate(batchDictionaryEntries, self.numSpins, device=device)
                Mx = torch.mean(allResults[1][0], axis=1)
                My = torch.mean(allResults[1][1], axis=1)
                Mxy[:,firstDictEntry:lastDictEntry] = Mx+(My*1j) 
                ReadoutMx = torch.mean(allResults[2][0], axis=1)
                ReadoutMy = torch.mean(allResults[2][1], axis=1)
                ReadoutMxy[:,firstDictEntry:lastDictEntry] = ReadoutMx+(ReadoutMy*1j)
                pbar.update(1)
        self.times = allResults[0]
        self.timeDomainResults = Mxy
        self.results = np.delete(ReadoutMxy,0,axis=0)
        return self.results
    
    @staticmethod
    def GetInnerProducts(querySignals, dictionarySignals):  
        """
        Calculate inner products between query and dictionary signals.

        Args:
            querySignals (numpy.ndarray): Query signals.
            dictionarySignals (numpy.ndarray): Dictionary signals.

        Returns:
            numpy.ndarray: Inner products between signals.
        """
        querySignalsTransposed = querySignals.transpose()
        normalizedQuerySignals = querySignalsTransposed / np.linalg.norm(querySignalsTransposed, axis=1)[:,None]
        simulationResultsTransposed = dictionarySignals.transpose()
        normalizedSimulationResultsTransposed = simulationResultsTransposed / np.linalg.norm(simulationResultsTransposed, axis=1)[:,None]
        innerProducts = np.inner(normalizedQuerySignals, normalizedSimulationResultsTransposed)
        return innerProducts

    def CalculateSVD(self, desiredSVDPower=0.99, truncationNumberOverride=None, clearUncompressedResults=False):
        """
        Perform Singular Value Decomposition (SVD) on simulation results.

        Args:
            desiredSVDPower (float, optional): Desired SVD power.
            truncationNumberOverride (int, optional): Override for truncation number.
            clearUncompressedResults (bool, optional): Clear uncompressed results.

        Returns:
            tuple: Truncation number and total SVD power.
        """
        dictionary = self.results.transpose()
        dictionaryNorm = np.sqrt(np.sum(np.power(np.abs(dictionary[:,:]),2),1))
        dictionaryShape = np.shape(dictionary)
        normalizedDictionary = np.zeros_like(dictionary)
        for i in range(dictionaryShape[0]):
            normalizedDictionary[i,:] = dictionary[i,:]/dictionaryNorm[i]
        (u,s,v) = np.linalg.svd(normalizedDictionary, full_matrices=False)
        self.singularValues = s
        if truncationNumberOverride == None:
            (truncationNumber, totalSVDPower) = self.GetTruncationNumberFromDesiredPower(desiredSVDPower)
        else:
            truncationNumber = truncationNumberOverride
            totalSVDPower = self.GetPowerFromDesiredTruncationNumber(truncationNumber)
        vt = np.transpose(v)
        self.truncationMatrix = vt[:,0:truncationNumber]
        self.truncatedResults = np.matmul(normalizedDictionary,self.truncationMatrix).transpose()
        if clearUncompressedResults:
            del self.results, self.times, self.timeDomainResults
        return (truncationNumber, totalSVDPower)

    def GetTruncationNumberFromDesiredPower(self, desiredSVDPower):
        """
        Get truncation number based on desired SVD power.

        Args:
            desiredSVDPower (float): Desired SVD power.

        Returns:
            tuple: Truncation number and total SVD power.
        """
        singularVectorPowers = self.singularValues/np.sum(self.singularValues)
        totalSVDPower=0; numSVDComponents=0
        for singularVectorPower in singularVectorPowers:
            totalSVDPower += singularVectorPower
            numSVDComponents += 1
            if totalSVDPower > desiredSVDPower:
                break
        return numSVDComponents, totalSVDPower

    def GetPowerFromDesiredTruncationNumber(self, desiredTruncationNumber):
        """
        Get total SVD power from desired truncation number.

        Args:
            desiredTruncationNumber (int): Desired truncation number.

        Returns:
            float: Total power.
        """
        singularVectorPowers = self.singularValues/np.sum(self.singularValues)
        totalSVDPower=np.sum(singularVectorPowers[0:desiredTruncationNumber])
        return totalSVDPower

    def Plot(self, dictionaryEntryNumbers=[], plotTruncated=False, plotTimeDomain=False):
        """
        Plot simulation results.

        Args:
            dictionaryEntryNumbers (list, optional): List of dictionary entry numbers.
            plotTruncated (bool, optional): Plot truncated results.
            plotTimeDomain (bool, optional): Plot in the time domain.

        Returns:
            None
        """
        if dictionaryEntryNumbers == []:
            dictionaryEntryNumbers = [int(len(self.dictionaryParameters.entries)/2)]
        ax = plt.subplot(1,1,1)
        if not plotTimeDomain:
            if not plotTruncated:
                for entry in dictionaryEntryNumbers:
                    plt.plot(abs(self.results[:,entry]), label=str(self.dictionaryParameters.entries[entry]))
            else:
                for entry in dictionaryEntryNumbers:
                    plt.plot(abs(self.truncatedResults[:,entry]), label=str(self.dictionaryParameters.entries[entry]))
        else:
            for entry in dictionaryEntryNumbers:
                plt.plot(self.times, abs(self.timeDomainResults[:,entry]), label=str(self.dictionaryParameters.entries[entry]))
        ax.legend()

    def GetAverageResult(self, indices):
        """
        Get the average result over specified indices.

        Args:
            indices (list): List of indices.

        Returns:
            numpy.ndarray: Average result.
        """
        return np.average(self.results[:,indices], 1)

    def FindPatternMatches(self, querySignals, useSVD=False, truncationNumber=25):
        """
        Find pattern matches in the simulation.

        Args:
            querySignals (numpy.ndarray): Query signals.
            useSVD (bool, optional): Use SVD for matching.
            truncationNumber (int, optional): Truncation number.

        Returns:
            numpy.ndarray: Indices of matched patterns.
        """
        if querySignals.ndim == 1:
            querySignals = querySignals[:,None]
        if not useSVD:
            querySignalsTransposed = querySignals.transpose()
            normalizedQuerySignal = querySignalsTransposed / np.linalg.norm(querySignalsTransposed, axis=1)[:,None]
            simulationResultsTransposed = self.results.transpose()
            normalizedSimulationResultsTransposed = simulationResultsTransposed / np.linalg.norm(simulationResultsTransposed, axis=1)[:,None]
            innerProducts = np.inner(normalizedQuerySignal, normalizedSimulationResultsTransposed)
            return np.argmax(abs(innerProducts), axis=1)
        else:
            if self.truncatedResults[:] == []:
                self.CalculateSVD(truncationNumber)
            signalsTransposed = querySignals.transpose()
            signalSVDs = np.matmul(signalsTransposed, self.truncationMatrix)
            normalizedQuerySignalSVDs = signalSVDs / np.linalg.norm(signalSVDs, axis=1)[:,None]
            simulationResultsTransposed = self.truncatedResults.transpose()
            normalizedSimulationResultsTransposed = simulationResultsTransposed / np.linalg.norm(simulationResultsTransposed, axis=1)[:,None]
            innerProducts = np.inner(normalizedQuerySignalSVDs, normalizedSimulationResultsTransposed)
            return np.argmax(abs(innerProducts), axis=1)