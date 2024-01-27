from ..Types import ReconstructionModuleIOType, ImageData, MapData
from . import ReconstructionModule, Register
import torch
import numpy as np


def GenerateMask(image, angularResolution=0.05, stepSize=4, fillSize=5, maxDecay=10, featheringKernelSize=3, threshold=0.75):
    coilMax = np.moveaxis(image,-1,0)
    threshold = np.mean(coilMax)*threshold
    maskIm = np.zeros(np.shape(coilMax))
    center = np.array(np.shape(coilMax)[1:3])/2
    Y, X = np.ogrid[:np.shape(coilMax)[2], :np.shape(coilMax)[1]]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)
    cylindricalMask = dist_from_center <= np.shape(coilMax)[1]/2
    coilMax = cylindricalMask*coilMax
    
    for partition in np.arange(0,np.shape(coilMax)[0]):
        for polarAngle in np.arange(0,2*np.pi, angularResolution):
            decayCounter = 0
            radius = 0
            historicalPos = []
            while decayCounter < maxDecay:
                radius += stepSize
                pos = (center + [radius*np.cos(polarAngle), radius*np.sin(polarAngle)]).astype(int)
                if(pos[0] > 0 and pos[0] < np.shape(coilMax)[1]-1 and pos[1] > 0 and pos[1] < np.shape(coilMax)[2]-1):
                    if coilMax[partition,pos[0],pos[1]] > threshold:
                        for histPos in historicalPos:
                            maskIm[partition, histPos[0]-fillSize:histPos[0]+fillSize, histPos[1]-fillSize:histPos[1]+fillSize] = 1
                        historicalPos.clear()
                        maskIm[partition, pos[0]-fillSize:pos[0]+fillSize, pos[1]-fillSize:pos[1]+fillSize] = 1
                        decayCounter = 0
                    else:
                        decayCounter += 1
                        historicalPos.append(pos)
                else:
                     break
    device = torch.device("cpu")
    maskIm = torch.tensor(maskIm).to(torch.float32)  
    meanFilter = torch.nn.Conv3d(in_channels=1, out_channels=1, kernel_size=featheringKernelSize, bias=False, padding='same')
    featheringKernelWeights = (torch.ones((featheringKernelSize, featheringKernelSize, featheringKernelSize), 
                                          dtype=torch.float32)/(featheringKernelSize*featheringKernelSize*featheringKernelSize)).to(device)
    meanFilter.weight.data = featheringKernelWeights.unsqueeze(0).unsqueeze(0)
    maskIm = meanFilter(maskIm.unsqueeze(0)).squeeze().detach().numpy()
    del featheringKernelWeights, meanFilter
    outputMask = np.moveaxis(maskIm, 0,-1)
    return outputMask

@Register
class IterativeRadialMaskingModule(ReconstructionModule):
   
    def __init__(self, reconstructionParameters, inputType:ReconstructionModuleIOType=ReconstructionModuleIOType.IMAGE, outputType:ReconstructionModuleIOType=ReconstructionModuleIOType.IMAGE, angularResolution=0.05, stepSize=4, fillSize=5, maxDecay=10, featheringKernelSize=3,threshold=0.75,device=None):

        ReconstructionModule.__init__(self, reconstructionParameters=reconstructionParameters, inputType=inputType, outputType=outputType) 
        self.angularResolution = angularResolution
        self.stepSize = stepSize
        self.fillSize = fillSize
        self.maxDecay = maxDecay
        self.featheringKernelSize = featheringKernelSize
        self.threshold = threshold
        if(device is None):
            self.device = reconstructionParameters.defaultDevice
        else:
            self.device = device

    def __dict__(self):
        """
        Convert module attributes to a dictionary.

        Returns:
            dict: Dictionary containing module attributes.
        """
        moduleDict  = {
            "type": str(self.__class__.__name__),
            "inputType": str(self.inputType.name),
            "outputType": str(self.outputType.name),
            "angularResolution" :  self.angularResolution,
            "stepSize" : self.stepSize,
            "fillSize" : self.fillSize,
            "maxDecay" : self.maxDecay,
            "featheringKernelSize": self.featheringKernelSize,
            "threshold" : self.threshold,
            "device": self.device.type
        }
        return moduleDict

    def ProcessMapToMap(self, inputData):
        """
        Process image data to image data by generating and applying a mask based on M0

        Args:
            inputData (ImageData): Input image data.

        Returns:
            ImageData: Processed image data.
        """
        with torch.no_grad():
            print("map2map")
            mask = GenerateMask(inputData["M0"], self.angularResolution, self.stepSize, self.fillSize, self.maxDecay, self.featheringKernelSize, self.threshold)
            return MapData(inputData*mask)

    def ProcessImageToImage(self, inputData):
        """
        Process image data to image data by generating and applying a mask

        Args:
            inputData (ImageData): Input image data.

        Returns:
            ImageData: Processed image data.
        """
        with torch.no_grad():
            print("image2image")
            mask = GenerateMask(inputData, self.angularResolution, self.stepSize, self.fillSize, self.maxDecay, self.featheringKernelSize, self.threshold)
            return ImageData(inputData*mask)
    
    @staticmethod
    def FromJson(jsonInput, reconstructionParameters, inputType, outputType):  
        
        device = jsonInput.get("device")
        angularResolution = jsonInput.get("angularResolution")
        stepSize = jsonInput.get("stepSize")
        fillSize = jsonInput.get("fillSize")
        maxDecay = jsonInput.get("maxDecay")
        featheringKernelSize = jsonInput.get("featheringKernelSize")
        threshold = jsonInput.get("threshold")
        if angularResolution != None and device != None:
            return IterativeRadialMaskingModule(reconstructionParameters, inputType, outputType,angularResolution,stepSize, fillSize, maxDecay, featheringKernelSize, threshold, torch.device(device))
        else:
            print("IterativeRadialMaskingModule requires mode and device")
        

    