from .Types import TrajectoryType, Units, TrajectoryUnits
from importlib.metadata import version  
import numpy as np
import json
from cxxheaderparser import simple
import numpy as np

class GradientWaveform:
    def __init__(self, maxGradStrength, xGrad, yGrad, zGrad=[], gradEndPad=0, dwellTime=2500, units=None):
        if(units != None):
            self.units = units
        else:
            self.units = TrajectoryUnits(Units.MILLITESLA_PER_METER, Units.MILLIMETERS)
        self.maxGradStrength = maxGradStrength
        self.xGrad = np.array(xGrad)
        self.yGrad = np.array(yGrad)
        self.zGrad = np.array(zGrad)
        self.gradEndPad = gradEndPad
        self.dwellTime = dwellTime
        self.numShots = self.xGrad.shape[0]
        self.numGradPts = self.xGrad.shape[1]

    def __dict__(self):
        """
        Returns a dictionary representation of the GradientWaveform object for the purposes of JSON serialization.

        Returns:
            dict: A dictionary representation of the object.
        """
        waveformDict  = {
            "units" : self.units.__dict__(),
            "maxGradStrength" : self.maxGradStrength, 
            "gradEndPad" : self.gradEndPad, 
            "dwellTime" : self.dwellTime, 
            "numGradPts" : self.numGradPts, 
            "numShots" : self.numShots, 
            "xGrad": self.xGrad.tolist(), 
            "yGrad": self.yGrad.tolist(), 
            "zGrad": self.zGrad.tolist() 
        }
        return waveformDict

    @staticmethod
    def FromJson(inputJson):
        """
        Create a GradientWaveform instance from a JSON string input.

        Args:
            inputJson (dict): JSON data containing GradientWaveform parameters.

        Returns:
            GradientWaveform: The created GradientWaveform instance.
        """
        unitsJson = inputJson.get("units")
        units = TrajectoryUnits.FromJson(unitsJson)
        maxGradStrength = inputJson.get("maxGradStrength")
        gradEndPad = inputJson.get("gradEndPad")
        dwellTime = inputJson.get("dwellTime")
        numGradPts = inputJson.get("numGradPts")
        numShots = inputJson.get("numShots")
        xGrad = inputJson.get("xGrad")
        yGrad = inputJson.get("yGrad")
        zGrad = inputJson.get("zGrad")
        
        if(unitsJson != None and maxGradStrength != None):
            return GradientWaveform(maxGradStrength, xGrad, yGrad, zGrad, gradEndPad, dwellTime, units )
        else:
            print("GradientWaveform requires units and maxGradStrength")

class TrajectoryParameters:
    def __init__(self, trajectoryType:TrajectoryType, fov, matrixSize, numShots, gradientWaveform:GradientWaveform, kspaceTrajectory=None, densityCompensation=None, name="", version="dev"):

        self.trajectoryType = trajectoryType
        self.fov = fov
        self.matrixSize = matrixSize
        self.numShots = numShots
        self.gradientWaveform = gradientWaveform
        self.kspaceTrajectory = kspaceTrajectory
        self.densityCompensation = densityCompensation
        self.version = version

        if not name:
            self.name = str(int(self.fov)) + "mm_" + str(int(self.matrixSize))+ "px_" + str(int(self.gradientWaveform.numShots)) + "shot"
        else:
            self.name = name

    def __dict__(self):
        """
        Returns a dictionary representation of the TrajectoryParameters object for the purposes of JSON serialization.

        Returns:
            dict: A dictionary representation of the object.
        """
        mrftools_version = version("mrftools")   
        if(self.kspaceTrajectory is not None):
            kspaceTrajectoryDict = {
                "real": self.kspaceTrajectory.real.tolist(), 
                "imag": self.kspaceTrajectory.imag.tolist()
            }
        else:
            kspaceTrajectoryDict = None
        if(self.densityCompensation is not None):
            densityCompensationDict = self.densityCompensation.tolist()
        else:
            densityCompensationDict = None

        trajectoryDict  = {
            "name" : self.name,
            "trajectoryType" : self.trajectoryType.name, 
            "version": self.version,
            "fov" : self.fov,
            "matrixSize" : self.matrixSize,
            "numShots" : self.numShots,
            "gradientWaveform" : self.gradientWaveform.__dict__(), 
            "kspaceTrajectory" : kspaceTrajectoryDict,
            "densityCompensation" : densityCompensationDict,
        }
        trajectoryParametersDict = {
            "mrftools_version": mrftools_version,
            "trajectory": trajectoryDict
        }
        return trajectoryParametersDict

    def ExportToJson(self, baseFilepath=""):
        """
        Export trajectory parameters to a JSON file.

        Args:
            baseFilepath (str, optional): Base filepath for the JSON file.

        Returns:
            None
        """
        trajectoryFilename = baseFilepath+self.name+"_"+self.version+".trajectory"
        with open(trajectoryFilename, 'w') as outfile:
            json.dump(self.__dict__(), outfile, indent=2)
        return trajectoryFilename

    @staticmethod
    def FromJson(inputJson):
        """
        Create a TrajectoryParameters instance from a JSON string input.

        Args:
            inputJson (dict): JSON data containing trajectory parameters.

        Returns:
            TrajectoryParameters: The created TrajectoryParameters instance.
        """
        mrftoolsVersion = inputJson.get("mrftools_version")
        if(mrftoolsVersion != None):
            #print("Input file mrttools Version:", mrftoolsVersion)
            trajectoryJson = inputJson.get("trajectory")
        else:
            trajectoryJson = inputJson
        name = trajectoryJson.get("name")
        version = trajectoryJson.get("version")
        waveformJson = trajectoryJson.get("gradientWaveform")
        gradientWaveform = GradientWaveform.FromJson(waveformJson)
        kspaceTrajectoryJson = trajectoryJson.get("kspaceTrajectory")
        kspaceTrajectory = None
        if(kspaceTrajectoryJson):
            kspaceTrajectory = np.array(kspaceTrajectoryJson.get("real")) + 1j * np.array(kspaceTrajectoryJson.get("imag"))
        densityCompensation = np.array(trajectoryJson.get("densityCompensation"))
        trajectoryType = TrajectoryType[trajectoryJson.get("trajectoryType")]
        fov = trajectoryJson.get("fov")
        matrixSize = trajectoryJson.get("matrixSize")
        numShots = trajectoryJson.get("numShots")
        
        if(name != None and trajectoryJson != None):
            return TrajectoryParameters(trajectoryType, fov, matrixSize, numShots, gradientWaveform, kspaceTrajectory, densityCompensation, name, version)
        else:
            print("TrajectoryParameters requires name and trajectory")

    @staticmethod
    def FromFile(path):
        """
        Create a TrajectoryParameters instance from a JSON file.

        Args:
            path (str): Path to the JSON file.

        Returns:
            TrajectoryParameters: The created TrajectoryParameters instance.
        """
        with open(path) as inputFile:
            inputJson = json.load(inputFile)
            return TrajectoryParameters.FromJson(inputJson)

    @staticmethod
    def FromCPPHeader(trajectoryType:TrajectoryType, headerFile):
        varDict = {}
        indentLevel = 0
        multiplier = 1
        for var in simple.parse_file(headerFile).namespace.variables:
            name = var.name.segments[0].name
            valArray = []
            tokens = var.value.tokens
            for i in np.arange(0, len(tokens)):
                current = tokens[i].value
                if current == "{":
                    indentLevel += 1
                elif current == "}":
                    indentLevel -= 1
                else:
                    if current == ",":
                        continue
                    elif(current == "-"):
                        multiplier = -1  
                    else:
                        valArray.append(multiplier * float(current.removesuffix("F")))  
                        multiplier = 1 
            if len(valArray) == 1:
                varDict[name] = valArray[0]
            else:
                varDict[name] = np.array(valArray)
        varDict['Xgrad'] = varDict['Xgrad'].reshape((int(varDict['NUMSHOTS']), -1))
        varDict['Ygrad'] = varDict['Ygrad'].reshape((int(varDict['NUMSHOTS']), -1))
        varDict['Xgrad'] = varDict['Xgrad'].tolist()
        varDict['Ygrad'] = varDict['Ygrad'].tolist()

        # Temporarily only allow 2D
        varDict["Zgrad"] = []

        #dict_keys(['Xgrad', 'Ygrad', 'NUMGRADPTS', 'NUMSHOTS', 'MAX_GRAD_STRENGTH', 'GRAD_END_PAD', 'DWELL_TIME', 'FOV', 'MATRIX_SIZE'])
        gradientWaveform = GradientWaveform(varDict["MAX_GRAD_STRENGTH"], varDict["Xgrad"], varDict["Ygrad"], varDict["Zgrad"], varDict["GRAD_END_PAD"], varDict["DWELL_TIME"])
        return TrajectoryParameters(trajectoryType, varDict["FOV"], varDict["MATRIX_SIZE"], varDict["NUMSHOTS"], gradientWaveform)
