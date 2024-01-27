import numpy as np
import h5py
from matplotlib import pyplot as plt
from importlib.metadata import version  
import json as json
from .Types import DictionaryEntry

class DictionaryParameters:
    """
    A class to manage dictionary parameters for MRF dictionary simulations.
    """

    def __init__(self, name, entries=[], version="dev"):
        """
        Initialize a DictionaryParameters object.

        Parameters
        ----------
        name : str
            Name of the dictionary.
        entries : numpy.ndarray, optional
            Numpy array containing dictionary entries, by default an empty array.
        version : str, optional
            Version of the dictionary, by default "dev".
        """
        self.name = name
        self.entries = entries
        self.version = version

    def __str__(self):
        """
        Returns a string representation of the number of entries in the dictionary.

        Returns
        -------
        str
            A string representation of the number of entries.
        """
        return "(" + str(len(self.entries)) + ")"
    

    def __dict__(self):
        """
        Returns a dictionary representation of the DictionaryParameters object for the purposes of JSON export

        Returns
        -------
        dict
            A dictionary representation of the object.
        """
        mrftools_version = version("mrftools")
        entryDict = [dict(zip(self.entries.dtype.names,x.tolist())) for x in self.entries]
        dictionaryDict  = {
            "name": self.name,
            "version": self.version,
            "entries": entryDict,
        }

        dictionaryParametersDict = {
            "mrftools_version": mrftools_version,
            "dictionary": dictionaryDict
        }
        return dictionaryParametersDict

    @staticmethod
    def FromJson(inputJson):
        """
        Creates a DictionaryParameters object from a JSON string input.

        Parameters
        ----------
        inputJson : dict
            JSON input containing dictionary information.

        Returns
        -------
        DictionaryParameters
            A new DictionaryParameters object created from the input JSON.
        """

        mrftoolsVersion = inputJson.get("mrftools_version")
        if(mrftoolsVersion != None):
            dictionaryJson = inputJson.get("dictionary")
        else:
            dictionaryJson = inputJson
        name = dictionaryJson.get("name")
        version = dictionaryJson.get("version")
        entriesJson = dictionaryJson.get("entries")
        if(name != None and entriesJson != None):
            entries = []
            for entryJson in entriesJson:
                entries.append(tuple(entryJson.values()))
            entries = np.array(entries, dtype=DictionaryEntry)         
            return DictionaryParameters(name, entries, version=version)   
        else:
            print("DictionaryParameters requires name and entries")

    @staticmethod
    def FromFile(path):
        """
        Creates a DictionaryParameters object from a JSON file.

        Parameters
        ----------
        path : str
            Path to the JSON file.

        Returns
        -------
        DictionaryParameters
            A new DictionaryParameters object created from the JSON file.
        """

        with open(path) as inputFile:
            inputJson = json.load(inputFile)
            return DictionaryParameters.FromJson(inputJson)

    def ExportToJson(self, baseFilepath=""):
        """
        Exports the dictionary to a JSON file.

        Parameters
        ----------
        baseFilepath : str, optional
            Base filepath for the JSON file, by default an empty string.
        """
        dictionaryFilename = baseFilepath+self.name+"_"+self.version+".dictionary"
        with open(dictionaryFilename, 'w') as outfile:
            json.dump(self.__dict__(), outfile, indent=2)

    def Initialize(self, T1s, T2s, B1s=[1]):
        """
        Initializes the dictionary with T1, T2, and (optionally) B1 values.

        Parameters
        ----------
        T1s : list or numpy.ndarray
            List or array of T1 values.
        T2s : list or numpy.ndarray
            List or array of T2 values.
        B1s : list or numpy.ndarray, optional
            List or array of B1 values, by default [1].
        """
        if (len(T1s)!=len(T2s)):
            print("Import Failed: T1/T2 lists must have identical number of entries")
            return 
        if (len(B1s) != len(T1s)):
            # B1 lists has different number of entries - tiling T1/T2 across B1
            self.entries = np.empty(len(T1s)*len(B1s), dtype=DictionaryEntry)
            for b1Index in range(len(B1s)):
                for t1Index in range(len(T1s)):
                    index = b1Index*len(T1s) + t1Index
                    self.entries[index] = (T1s[t1Index], T2s[t1Index], B1s[b1Index])
        else:
            # T1/T2/B1 lists have same number of entries - reading entries 1:1
            self.entries = np.empty(len(T1s), dtype=DictionaryEntry)
            for t1Index in range(len(T1s)):
                self.entries[t1Index] = (T1s[t1Index], T2s[t1Index], B1s[t1Index])

    def InitializeFromUnique(self, T1s, T2s, B1s=[1]):
        """
        Initializes the dictionary with unique T1, T2, and (optionally) B1 values, generating all combinations

        Parameters
        ----------
        T1s : list or numpy.ndarray
            List or array of unique T1 values.
        T2s : list or numpy.ndarray
            List or array of unique T2 values.
        B1s : list or numpy.ndarray, optional
            List or array of unique B1 values, by default [1].
        """

        # Create dictionary parameter definition programmatically
        dictionaryEntries = np.ones(len(T1s)*len(T2s)*len(B1s), dtype=DictionaryEntry)
        for b1Index in np.arange(len(B1s)):
            for t1Index in np.arange(len(T1s)):
                for t2Index in np.arange(len(T2s)):
                    currentIndex = b1Index * len(T1s) * len(T2s) +  t1Index * len(T2s) + t2Index
                    dictionaryEntries[currentIndex]['T1'] = T1s[t1Index]
                    dictionaryEntries[currentIndex]['T2'] = T2s[t2Index]
                    dictionaryEntries[currentIndex]['B1'] = B1s[b1Index]
        self.entries = dictionaryEntries

    
    def Plot(self):
        """
        Creates a plot of T1 vs T2 values.
        """
        plt.plot(self.entries['T1'], self.entries['T2'])

    def GetNearestEntry(self, T1, T2, B1=1):
        """
        Returns the index and entry closest to the given T1, T2, and B1 values.

        Parameters
        ----------
        T1 : float
            T1 value.
        T2 : float
            T2 value.
        B1 : float, optional
            B1 value, by default 1.

        Returns
        -------
        tuple
            A tuple containing the index and the nearest entry.
        """
        T1diff = np.absolute(self.entries['T1']-T1)
        T2diff = np.absolute(self.entries['T2']-T2)
        B1diff = np.absolute(self.entries['B1']-B1)
        diffs = np.squeeze(np.dstack([T1diff,T2diff,B1diff]))
        normedDiffs = np.linalg.norm(diffs,axis=1)
        index = np.argmin(normedDiffs)
        return (index, self.entries[index])

    def GetRegionNear(self, T1, T2, B1=1, T1Radius=-1, T2Radius=-1, B1Radius=-1):
        """
        Returns entries within a radius of the given T1, T2, and B1 values.

        Parameters
        ----------
        T1 : float
            T1 value.
        T2 : float
            T2 value.
        B1 : float, optional
            B1 value, by default 1.
        T1Radius : float, optional
            T1 radius, by default -1.
        T2Radius : float, optional
            T2 radius, by default -1.
        B1Radius : float, optional
            B1 radius, by default -1.

        Returns
        -------
        tuple
            A tuple containing the list of indices and corresponding entries.
        """
        if T1Radius == -1:
            T1Radius = T1*0.1
        if T2Radius == -1:
            T2Radius = T2*0.1
        if B1Radius == -1:
            B1Radius = B1*0.1

        T1Indices = np.squeeze(np.where(np.absolute(self.entries['T1']-T1) < T1Radius))    
        T2Indices = np.squeeze(np.where(np.absolute(self.entries['T2']-T2) < T2Radius))
        B1Indices = np.squeeze(np.where(np.absolute(self.entries['B1']-B1) < B1Radius))

        resultList = list(set(T1Indices) & set(T2Indices) & set(B1Indices))
        return (resultList, self.entries[resultList])

    @staticmethod
    def ImportFromTxt(name, T1Filepath, T2Filepath, B1Filepath="", version="dev"):
        """
        Imports a DictionaryParameters object from text files.

        Parameters
        ----------
        name : str
            Name of the dictionary.
        T1Filepath : str
            Path to the T1 values text file.
        T2Filepath : str
            Path to the T2 values text file.
        B1Filepath : str, optional
            Path to the B1 values text file, by default an empty string.
        version : str, optional
            Version of the dictionary, by default "dev".

        Returns
        -------
        DictionaryParameters
            A new DictionaryParameters object created from the text files.
        """
        new_dictionary_parameters = DictionaryParameters(name, version=version)
        T1s = np.loadtxt(T1Filepath)
        T2s = np.loadtxt(T2Filepath)
        if(B1Filepath != ""):
            B1s = np.loadtxt(B1Filepath)
            new_dictionary_parameters.Initialize(T1s, T2s, B1s)
        else:
            new_dictionary_parameters.Initialize(T1s,T2s)
        return new_dictionary_parameters

    @staticmethod
    def GenerateFixedPercent(name, t1Range=(100,4000), t2Range=(1,400), percentStepSize=5, includeB1=False, b1Range=(0.5,1.5), b1Stepsize=0.05, version="dev"):
        """
        Generates a dictionary with fixed percentage step sizes.

        Parameters
        ----------
        name : str
            Name of the dictionary.
        t1Range : tuple, optional
            Range of T1 values, by default (100, 4000).
        t2Range : tuple, optional
            Range of T2 values, by default (1, 400).
        percentStepSize : int, optional
            Percentage step size, by default 5.
        includeB1 : bool, optional
            Include B1 values if True, by default False.
        b1Range : tuple, optional
            Range of B1 values, by default (0.5, 1.5).
        b1Stepsize : float, optional
            B1 step size, by default 0.05.
        version : str, optional
            Version of the dictionary, by default "dev".

        Returns
        -------
        DictionaryParameters
            A new DictionaryParameters object generated with fixed percentage step sizes.
        """
        new_dictionary_parameters = DictionaryParameters(name, version=version)
        T1s = []
        T2s = []
        t1 = t1Range[0]
        t2 = t2Range[0]
        while t1 <= t1Range[1]:
            T1s.append(t1/1000)
            t1 = t1*(1+(percentStepSize/100))
        while t2 <= t2Range[1]:
            T2s.append(t2/1000)
            t2 = t2*(1+(percentStepSize/100))
        pairs = []
        for t1Val in T1s:
            for t2Val in T2s:
                if(t1Val>t2Val): # Don't include pairs with T2 longer than T1
                    pairs.append((t1Val,t2Val))
        T1sFromPairs = []
        T2sFromPairs = []
        for pair in pairs:
            T1sFromPairs.append(pair[0])
            T2sFromPairs.append(pair[1])
        if(includeB1):
            B1s = np.arange(b1Range[0], b1Range[1], b1Stepsize)
            new_dictionary_parameters.Initialize(T1sFromPairs,T2sFromPairs, B1s)
        else:
            new_dictionary_parameters.Initialize(T1sFromPairs, T2sFromPairs)
        return new_dictionary_parameters

    @staticmethod
    def GenerateFixedStep(name, t1Range=(100,4000), t2Range=(1,400), fixedStepSize=1, includeB1=False, b1Range=(0.5,1.5), b1Stepsize=0.05,  version="dev"):
        """
        Generates a dictionary with fixed step sizes.

        Parameters
        ----------
        name : str
            Name of the dictionary.
        t1Range : tuple, optional
            Range of T1 values, by default (100, 4000).
        t2Range : tuple, optional
            Range of T2 values, by default (1, 400).
        fixedStepSize : int, optional
            Fixed step size, by default 1.
        includeB1 : bool, optional
            Include B1 values if True, by default False.
        b1Range : tuple, optional
            Range of B1 values, by default (0.5, 1.5).
        b1Stepsize : float, optional
            B1 step size, by default 0.05.
        version : str, optional
            Version of the dictionary, by default "dev".

        Returns
        -------
        DictionaryParameters
            A new DictionaryParameters object generated with fixed step sizes.
        """
        new_dictionary_parameters = DictionaryParameters(name, version=version)
        T1s = []
        T2s = []
        t1 = t1Range[0]
        t2 = t2Range[0]
        while t1 <= t1Range[1]:
            T1s.append(t1/1000)
            t1 = t1+fixedStepSize
        while t2 <= t2Range[1]:
            T2s.append(t2/1000)
            t2 = t2+fixedStepSize
        pairs = []
        for t1Val in T1s:
            for t2Val in T2s:
                if(t1Val>t2Val): # Don't include pairs with T2 longer than T1
                    pairs.append((t1Val,t2Val))
        T1sFromPairs = []
        T2sFromPairs = []
        for pair in pairs:
            T1sFromPairs.append(pair[0])
            T2sFromPairs.append(pair[1])
        if(includeB1):
            B1s = np.arange(b1Range[0], b1Range[1], b1Stepsize)
            new_dictionary_parameters.Initialize(T1sFromPairs,T2sFromPairs, B1s)
        else:
            new_dictionary_parameters.Initialize(T1sFromPairs, T2sFromPairs)
        return new_dictionary_parameters



