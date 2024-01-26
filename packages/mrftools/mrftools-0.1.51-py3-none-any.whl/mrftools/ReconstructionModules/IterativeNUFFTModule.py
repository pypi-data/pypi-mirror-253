from . import NUFFTModule
from ..Types import ReconstructionModuleIOType, ImageData
from . import ReconstructionModule, Register
import torch
import numpy as np
import mrftools.Utilities.torchkbnufft as tkbn
import ptwt
import collections
from .CoilCombinationModule import calculateCoilmapsWalsh

class IterativeNUFFTModule(NUFFTModule):

    def __init__(self, reconstructionParameters, 
                 inputType:ReconstructionModuleIOType=ReconstructionModuleIOType.KSPACE, outputType:ReconstructionModuleIOType=ReconstructionModuleIOType.IMAGE, 
                 ktraj=None, dcf=None, numNearestNeighbors=3, device=None, initializeWithDCF=False, useDCFInIterations=False, readoutTruncationLimit=-1, 
                 maskingMode="iterative_radius_spherical", maxIterations=10, gradTolerance=1e-6,
                 maxLinesearchIterations=3, t0=0.1, alpha=0.125, beta=0.5, maxSingleSteps=2, t0Max=-1,
                 waveletLambda=0,  waveletType='db2', waveletLevel=4):
        """
        Initialize the NUFFTModule.

        Args:
            reconstructionParameters (dict): Parameters specific to the reconstruction module.
            inputType (ReconstructionModuleIOType, optional): Input data type.
            outputType (ReconstructionModuleIOType, optional): Output data type.
            ktraj (torch.Tensor, optional): k-space trajectory.
            dcf (torch.Tensor, optional): Density compensation factor.
            numNearestNeighbors (int, optional): Number of nearest neighbors for NUFFT.
            initializeWithDCF (bool, optional): Initialize with density compensation factor.
            useDCFInIterations (bool, optional): Use density compensation factor in iterations.
            readoutTruncationLimit (int, optional): Readout truncation limit.
            maskingMode (str, optional): Masking mode.
            maxIterations (int, optional): Maximum number of iterations.
            gradTolerance (float, optional): Gradient tolerance.
            maxLinesearchIterations (int, optional): Maximum line search iterations.
            t0 (float, optional): Initial time step.
            alpha (float, optional): Alpha parameter.
            beta (float, optional): Beta parameter.
            maxSingleSteps (int, optional): Maximum single steps.
            t0Max (float, optional): Maximum time step.
            waveletLambda (float, optional): Wavelet lambda parameter.
            waveletType (str, optional): Wavelet type.
            waveletLevel (int, optional): Wavelet level.
        """
        NUFFTModule.__init__(self, reconstructionParameters=reconstructionParameters, inputType=inputType, outputType=outputType, ktraj=ktraj, dcf=dcf, numNearestNeighbors=numNearestNeighbors, device=device) 
        self.initializeWithDCF = initializeWithDCF
        self.useDCFInIterations = useDCFInIterations
        self.readoutTruncationLimit = readoutTruncationLimit
        self.maskingMode = maskingMode
        self.maxIterations = maxIterations
        self.gradTolerance = gradTolerance
        self.maxLinesearchIterations = maxLinesearchIterations
        self.t0 = t0
        self.alpha = alpha
        self.beta = beta
        self.maxSingleSteps = maxSingleSteps
        self.t0Max = t0Max
        self.waveletLambda = waveletLambda
        self.waveletType = waveletType
        self.waveletLevel = waveletLevel


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
            "ktraj": self.ktraj.tolist(),
            "dcf": self.dcf.tolist(),
            "numNearestNeighbors": self.numNearestNeighbors,
            "device": self.device.type,
            "initializeWithDCF" : self.initializeWithDCF,
            "useDCFInIterations" : self.useDCFInIterations,
            "readoutTruncationLimit" : self.readoutTruncationLimit,
            "maskingMode" : self.maskingMode,
            "maxIterations" : self.maxIterations,
            "gradTolerance" : self.gradTolerance,
            "maxLinesearchIterations" : self.maxLinesearchIterations,
            "t0" : self.t0,
            "alpha" : self.alpha,
            "beta" : self.beta,
            "maxSingleSteps" : self.maxSingleSteps,
            "t0Max" : self.t0Max,
            "waveletLambda" : self.waveletLambda,
            "waveletType" : self.waveletType,
            "waveletLevel" : self.waveletLevel,
        }
        return moduleDict

    def ApplyNormalization(self, imageData):
        """
        Apply normalization to the input image data and the raw data.

        Args:
            imageData (torch.Tensor): Input image data.

        Returns:
            tuple: A tuple containing the normalized image data and the normalized raw data.
        """
        scaling = torch.max(torch.abs(imageData).flatten())
        return imageData/scaling, self.rawData/scaling
    
    def ExpandCoils(self, imageData):
        """
        Expand coils by multiplying the input image data with coilmaps.

        Args:
            imageData (torch.Tensor): Input image data.

        Returns:
            torch.Tensor: Expanded image data after coil multiplication.
        """
        with torch.no_grad():
            for svdComponent in range(0, self.numSVDComponents):
                for coil in range(0,self.numCoils):
                    self.images[svdComponent,coil,:,:,:] = (imageData.moveaxis(3,1)[svdComponent,:,:] * self.coilmaps[coil,:,:,:])
            return self.images

    def CombineCoils(self, coilImageData):
        """
        Combine coil images using coilmaps.

        Args:
            coilImageData (torch.Tensor): Coil image data.

        Returns:
            torch.Tensor: Combined image data.
        """
        with torch.no_grad():
            combinedImageData = torch.zeros((self.numSVDComponents, self.numPartitions, self.matrixSize[0], self.matrixSize[1]), dtype=torch.complex64).to(self.device)
            for svdComponent in np.arange(0,self.numSVDComponents):
                im = coilImageData[svdComponent, :, :, :, :]
                combinedImageData[svdComponent, :, :, :] = torch.sum((im * torch.conj(self.coilmaps)), axis=0)
                del im
            combinedImageData = combinedImageData.moveaxis(1,-1)
            return combinedImageData

    # Input should have shape [svdComponents, coils, partitions, matrixX, matrixY]
    # Output should have shape [svdComponents, coils, partitions, matrixX, matrixY]
    def PerformThroughplaneFFT(self, input):
        """
        Perform through-plane FFT on the input data.

        Args:
            input (torch.Tensor): Input data.

        Returns:
            torch.Tensor: Data after performing through-plane FFT.
        """
        with torch.no_grad():
            for svdComponent in np.arange(0, self.numSVDComponents):
                for coil in np.arange(0,self.numCoils):
                    temp_device = input[svdComponent,coil,:,:,:].to(self.images.device)
                    self.images[svdComponent,coil,:,:,:] = torch.fft.ifftshift(torch.fft.fft(torch.fft.fftshift(temp_device, dim=0), dim=0, norm="ortho"), dim=0)
                    del temp_device
            return self.images

    # Input should have shape [svdComponents, coils, partitions, matrixX, matrixY]
    # Output should have shape [svdComponents, coils, partitions, matrixX, matrixY]
    def PerformThroughplaneIFFT(self, input):
        """
        Perform through-plane inverse FFT on the input data.

        Args:
            input (torch.Tensor): Input data.

        Returns:
            torch.Tensor: Data after performing through-plane inverse FFT.
        """
        with torch.no_grad():
            for svdComponent in np.arange(0, self.numSVDComponents):
                for coil in np.arange(0,self.numCoils):
                    temp_device = input[svdComponent,coil,:,:,:].to(self.images.device)
                    self.images[svdComponent,coil,:,:,:] = torch.fft.fftshift(torch.fft.ifft(torch.fft.ifftshift(temp_device, dim=0), dim=0, norm="ortho"), dim=0)
                    del temp_device
            return self.images

    # Input should have shape [svdComponents, coils, partitions, readoutPoints, spirals]
    # Output should have shape [svdComponents, coils, partitions, matrixX, matrixY]
    def PerformAdjointNUFFTs(self, input, applyDCF=False):
        """
        Perform adjoint non-uniform fast Fourier transform (NUFFT) on input data.

        Args:
            input (torch.Tensor): Input data.
            applyDCF (bool, optional): Apply density compensation factor. Default is False.

        Returns:
            torch.Tensor: Image data after performing adjoint NUFFT.
        """
        for partition in np.arange(0,self.numPartitions):
            if(applyDCF or self.useDCFInIterations):
                readout_device = torch.swapaxes(input[:, :, partition, :, :], -1,-2).reshape(self.numSVDComponents, self.numCoils, -1).to(self.images.device) * self.sqrt_dcf
            else: 
                readout_device = torch.swapaxes(input[:, :, partition, :, :], -1,-2).reshape(self.numSVDComponents, self.numCoils, -1).to(self.images.device)
            nufftResult = self.adjoint_nufft(readout_device, self.ktraj, norm="ortho")
            self.images[:,:,partition,:,:] = nufftResult
            del readout_device, nufftResult
                #pbar.update(1)
        return self.images

    # Input should have shape [svdComponents, coils, partitions, matrixX, matrixY]
    # Output should have shape [svdComponents, coils, partitions, readoutPoints, spirals]
    def PerformNUFFTs(self, input, applyDCF=False):
        """
        Perform non-uniform fast Fourier transform (NUFFT) on input data.

        Args:
            input (torch.Tensor): Input data.
            applyDCF (bool, optional): Apply density compensation factor. Default is False.

        Returns:
            torch.Tensor: Image data after performing NUFFT.
        """
        with torch.no_grad():
            for partition in np.arange(0,self.numPartitions):
                image_device = input[:, :, partition, :, :].to(self.svdSpace.device)
                if(applyDCF or self.useDCFInIterations):
                    nufftResult = self.nufft(image_device, self.ktraj, norm="ortho") * self.sqrt_dcf
                else:
                    nufftResult = self.nufft(image_device, self.ktraj, norm="ortho")
                self.svdSpace[:,:,partition,:,:] = torch.swapaxes(nufftResult.reshape(self.numSVDComponents,self.numCoils,self.numSpirals, self.numReadoutPoints), -1,-2)
                del image_device, nufftResult
                    #pbar.update(1)
        return self.svdSpace

    def PartitionwiseDifference(self, minuend, subtrahend):
        """
        Compute the partition-wise difference between `minuend` and `subtrahend`.

        Args:
            minuend (torch.Tensor): The minuend tensor with shape [coils, partitions, readouts, spirals, spiralTimepoints].
            subtrahend (torch.Tensor): The subtrahend tensor with shape [coils, partitions, readouts, spirals, spiralTimepoints].

        Returns:
            torch.Tensor: The result tensor containing the partition-wise differences, with the same shape as `minuend`.
        """
        with torch.no_grad():
            for partition in np.arange(0,self.numPartitions):
                subtrahendTemp = subtrahend[:,:,partition, :,:].to(minuend.device)
                minuend[:,:,partition, :,:] = minuend[:,:,partition, :,:] - subtrahendTemp
                del subtrahendTemp
            return minuend

    def PartitionwiseSumOfSquaredAbs(self, input):
        """
        Compute the partition-wise sum of squared absolute values of the input tensor.

        Args:
            input (torch.Tensor): The input tensor with shape [coils, partitions, readouts, spirals, spiralTimepoints].

        Returns:
            torch.Tensor: The sum of squared absolute values for each partition.
        """
        with torch.no_grad():
            sum = 0
            for partition in np.arange(0,self.numPartitions):
                sum += torch.sum(torch.abs(input[:,:,partition, :,:]**2))
            return sum

    # Raw Data should have shape [coil, partitions, readouts, spirals, spiralTimepoints]
    def ApplySVDCompression(self, rawdata):
        """
        Apply Singular Value Decomposition (SVD) compression to the raw data.

        Args:
            rawdata (torch.Tensor): The raw data tensor with shape [coils, partitions, readouts, spirals, spiralTimepoints].

        Returns:
            torch.Tensor: The compressed data tensor after applying SVD compression, with shape [coils, partitions, readouts, spirals, numSVDComponents].
        """
        with torch.no_grad():
            for spiral in np.arange(0,self.numSpirals):
                truncationMatrix = torch.zeros((self.numTimepointsPerSpiral, self.numSVDComponents), dtype=torch.complex64)
                for spiralTimepoint in np.arange(0,self.numTimepointsPerSpiral):
                    realTimepoint = self.numSpirals*spiralTimepoint + spiral
                    truncationMatrix[spiralTimepoint, :] = torch.tensor(self.simulation.truncationMatrix[realTimepoint, :])
                result = torch.moveaxis(torch.matmul(rawdata[:,:,:,spiral,:].to(torch.complex64), truncationMatrix), -1, 0).to(self.svdSpace.device)
                self.svdSpace[:,:, :, :, spiral] = result
                del truncationMatrix, result
            return self.svdSpace

    # svdData should have shape [svdComponents, coils, partitions, readoutPoints, spirals]
    def UnapplySVDCompression(self, svdData):
        """
        Unapply Singular Value Decomposition (SVD) compression to expand the compressed data back to the original raw data space.

        Args:
            svdData (torch.Tensor): The compressed data tensor with shape [svdComponents, coils, partitions, readoutPoints, spirals].

        Returns:
            torch.Tensor: The reconstructed k-space data tensor after undoing SVD compression, with shape [coils, partitions, readoutPoints, spirals, spiralTimepoints].
        """
        with torch.no_grad():
            for spiral in np.arange(0,self.numSpirals):
                truncationMatrix = torch.zeros((self.numTimepointsPerSpiral, self.numSVDComponents), dtype=torch.complex64)
                for spiralTimepoint in np.arange(0,self.numTimepointsPerSpiral):
                    realTimepoint = self.numSpirals*spiralTimepoint + spiral
                    truncationMatrix[spiralTimepoint, :] = torch.tensor(self.simulation.truncationMatrix[realTimepoint, :])
                input = torch.moveaxis(svdData[:,:, :, :, spiral], 0, -1).to(self.kspace.device)
                self.kspace[:,:,:,spiral,:] = torch.matmul(input, truncationMatrix.t())
                del truncationMatrix, input
            return self.kspace

    def L2Gradient(self, x):
        """
        Compute the L2 regularization gradient for the input tensor `x`.

        Args:
            x (torch.Tensor): The input tensor.

        Returns:
            torch.Tensor: The L2 regularization gradient tensor.
        """
        with torch.no_grad():
            E_x = self.UnapplySVDCompression(self.PerformNUFFTs(self.PerformThroughplaneFFT(self.ExpandCoils(x))))
            E_x[self.rawDataMask] = E_x[self.rawDataMask] - self.rawData
            E_x[self.rawDataMask == 0] = 0
            result = 2 * self.CombineCoils(self.PerformThroughplaneIFFT(self.PerformAdjointNUFFTs(self.ApplySVDCompression(E_x))))
            return result

    def WaveletGradient(self, x):
        """
        Compute the wavelet regularization gradient for the input tensor `x`.

        Args:
            x (torch.Tensor): The input tensor.

        Returns:
            torch.Tensor: The wavelet regularization gradient tensor.
        """
        l1Smooth = 1e-15
        with torch.no_grad():
            if(self.waveletLambda > 0):
                grad = torch.zeros_like(x)
                with torch.no_grad():
                    for svdComponent in np.arange(0,self.numSVDComponents):
                        coeffs_real_dev = ptwt.wavedec3(x[svdComponent,:,:,:].real, self.waveletType, level=self.waveletLevel)
                        coeffs_imag_dev = ptwt.wavedec3(x[svdComponent,:,:,:].imag, self.waveletType, level=self.waveletLevel)
                        coeffs_real_dev[0] = torch.zeros_like(coeffs_real_dev[0])
                        coeffs_imag_dev[0] = torch.zeros_like(coeffs_imag_dev[0])
                        for level in range(1,len(coeffs_real_dev)):
                            for component,_ in coeffs_real_dev[level].items():
                                coeffs = coeffs_real_dev[level][component] + 1.0j*coeffs_imag_dev[level][component]
                                coeffs = (coeffs * torch.pow((coeffs*torch.conj(coeffs)+l1Smooth),-0.5))
                                coeffs_real_dev[level][component] = coeffs.real
                                coeffs_imag_dev[level][component] = coeffs.imag
                                #coeffs_real_dev[level][component] *= 2
                                #coeffs_imag_dev[level][component] *= 2
                        grad[svdComponent,:,:,:] = ptwt.waverec3(coeffs_real_dev, self.waveletType) + 1.0j* ptwt.waverec3(coeffs_imag_dev, self.waveletType)
                        del coeffs_real_dev, coeffs_imag_dev
                    return grad
            else:
                return 0

    def Grad(self, x):
        """
        Compute the total gradient of the objective function for the input tensor `x`.

        Args:
            x (torch.Tensor): The input tensor.

        Returns:
            torch.Tensor: The total gradient tensor.
        """
        with torch.no_grad():
            result = self.L2Gradient(x) + self.waveletLambda * self.WaveletGradient(x)
            return result
    
    def L2Objective(self, x):
        """
        Compute the L2 regularization objective for the input tensor `x`.

        Args:
            x (torch.Tensor): The input tensor.

        Returns:
            torch.Tensor: The L2 regularization objective value.
        """
        E_x = self.UnapplySVDCompression(self.PerformNUFFTs(self.PerformThroughplaneFFT(self.ExpandCoils(x))))
        return torch.sum((torch.abs(E_x[self.rawDataMask] - self.rawData))**2)
    
    def WaveletObjective(self, x):
        """
        Compute the wavelet regularization objective for the input tensor `x`.

        Args:
            x (torch.Tensor): The input tensor.

        Returns:
            torch.Tensor: The wavelet regularization objective value.
        """
        l1Smooth = 1e-15
        if(self.waveletLambda > 0):
            sum = 0
            with torch.no_grad():
                for svdComponent in np.arange(0,self.numSVDComponents):
                    coeffs_real_dev = ptwt.wavedec3(x[svdComponent,:,:,:].real, self.waveletType, level=self.waveletLevel)
                    coeffs_imag_dev = ptwt.wavedec3(x[svdComponent,:,:,:].imag, self.waveletType, level=self.waveletLevel)
                    coeffs_real_dev[0] = torch.zeros_like(coeffs_real_dev[0])
                    coeffs_imag_dev[0] = torch.zeros_like(coeffs_imag_dev[0])
                    for level in range(1,len(coeffs_real_dev)):
                        for component,_ in coeffs_real_dev[level].items():
                            coeffs = coeffs_real_dev[level][component] + 1.0j*coeffs_imag_dev[level][component]
                            sum = sum + torch.sum(torch.pow((coeffs*torch.conj(coeffs)+l1Smooth),0.5))
                            #sum = sum + torch.sum(torch.abs(coeffs)**2)
                    del coeffs_real_dev, coeffs_imag_dev
                return torch.abs(sum) # Matlab doesn't take the abs, results in comparison of complex values
        else:
            return 0

    def Objective(self, x, dx, t): 
        """
        Compute the total objective function value and its components for the input tensor `x`.

        Args:
            x (torch.Tensor): The input tensor.
            dx (torch.Tensor): The gradient tensor.
            t (float): The step size.

        Returns:
            tuple: A tuple containing the total objective value, L2 regularization objective, and wavelet regularization objective.
        """
        with torch.no_grad():
            current = x + t*dx
            l2Objective = self.L2Objective(current)
            wavObjective = self.WaveletObjective(current)
            return l2Objective + self.waveletLambda * wavObjective, l2Objective, wavObjective

    def PrepMemoryObjects(self):
        """
        Initialize memory objects for storing images, SVD space, and k-space data.
        """
        self.images = torch.zeros((self.numSVDComponents, self.numCoils, self.numPartitions, self.matrixSize[0], self.matrixSize[1]), dtype=torch.complex64).to(self.device)
        self.svdSpace = torch.zeros((self.numSVDComponents, self.numCoils, self.numPartitions, self.numReadoutPoints, self.numSpirals), dtype=torch.complex64).to(self.device)
        self.kspace = torch.zeros((self.numCoils, self.numPartitions, self.numReadoutPoints, self.numSpirals, self.numTimepointsPerSpiral), dtype=torch.complex64)
        
    def PrepNufftObjects(self):
        """
        Initialize NUFFT objects for performing non-uniform Fourier transforms.
        """
        self.nufft = tkbn.KbNufft(im_size=tuple(self.matrixSize[0:2]), grid_size=tuple(self.gridSize[0:2]),numpoints=self.numNearestNeighbors).to(self.images.device)
        self.adjoint_nufft = tkbn.KbNufftAdjoint(im_size=tuple(self.matrixSize[0:2]), grid_size=tuple(self.matrixSize[0:2]),numpoints=self.numNearestNeighbors).to(self.images.device)

    def PrepCylindricalMask(self, edgePaddingPixels=2):
        """
        Prepare a cylindrical mask for image data.

        Args:
            edgePaddingPixels (int, optional): Number of pixels to exclude near the edges. Defaults to 2.

        Returns:
            torch.Tensor: The cylindrical mask.
        """
        maskIm = np.zeros((self.numSVDComponents,self.matrixSize[0], self.matrixSize[1], self.numPartitions), dtype=bool)
        center = np.array(np.shape(maskIm)[1:3])/2
        Y, X = np.ogrid[:np.shape(maskIm)[2], :np.shape(maskIm)[1]]
        dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)
        cylindricalMask = dist_from_center <= (np.shape(maskIm)[1]/2-edgePaddingPixels)
        for svdComponent in np.arange(0, self.numSVDComponents):
            for partition in np.arange(0,self.numPartitions):
                maskIm[svdComponent,:,:, partition] = cylindricalMask
        self.imageMask = torch.tensor(maskIm)
        return self.imageMask

    def PrepIterativeRadiusSphericalMask(self, svdNum = 0, angularResolution = 0.01, stepSize = 3, fillSize = 3, maxDecay = 15, featheringKernelSize=4):
        """
        Prepare an iterative radius spherical mask for image data.

        Args:
            svdNum (int, optional): SVD component number. Defaults to 0.
            angularResolution (float, optional): Angular resolution for the mask. Defaults to 0.01.
            stepSize (int, optional): Step size for radius iteration. Defaults to 3.
            fillSize (int, optional): Size of the region to fill in the mask. Defaults to 3.
            maxDecay (int, optional): Maximum number of decay iterations. Defaults to 15.
            featheringKernelSize (int, optional): Size of the feathering kernel. Defaults to 4.

        Returns:
            torch.Tensor: The spherical mask.
        """
        outputMask = np.zeros((self.numSVDComponents,self.matrixSize[0], self.matrixSize[1], self.numPartitions), dtype=bool)
        coilMax = np.abs(torch.moveaxis(self.imageData[svdNum,:,:,:].cpu(),2,0).numpy())
        threshold = np.mean(coilMax)
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
                            #maskIm[partition, pos[0]-fillSize:pos[0]+fillSize, pos[1]-fillSize:pos[1]+fillSize] = 1 - (decayCounter/maxDecay)
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
        mask = np.moveaxis(maskIm, 0,-1)
        for svdComponent in np.arange(0, self.numSVDComponents):
            outputMask[svdComponent,:,:, :] = mask
        self.imageMask = torch.tensor(outputMask)
        return self.imageMask    

    def FinalizeResults(self, destroyMemoryObjects=True):
        """
        Finalize the results and release memory objects if specified.

        Args:
            destroyMemoryObjects (bool, optional): Whether to destroy memory objects. Defaults to True.

        Returns:
            torch.Tensor: The finalized results.
        """
        results = self.imageData.cpu()
        del self.imageData, self.kspace, self.images, self.imageMask, self.nufft, self.adjoint_nufft, self.svdSpace, self.ktraj, self.dcf, self.sqrt_dcf
        return results
    
    def PerformWalshCoilCombination(self, input, kernelSize=(5,5,1), niter=5):
        """
        Perform Walsh coil combination on input data.

        Args:
            input (torch.Tensor): Input complex images
            kernelSize (tuple, optional): Smoothing block size. Defaults to (5, 5, 1).
            niter (int, optional): Number of iterations for the eigenvector power method. Defaults to 5.

        Returns:
            torch.Tensor: Combined complex image of shape [y, x, svdComponent].
        """
        with torch.no_grad():
            shape = np.shape(input)
            combinedImageData = torch.zeros((shape[0], shape[2], shape[3], shape[4]), dtype=torch.complex64)
            coil_map, rho = calculateCoilmapsWalsh(input[0,:,:,:,:], smoothing=kernelSize, niter=niter, device=self.device)
            for svdComponent in np.arange(0,shape[0]):
                im = (input[svdComponent, :, :, :, :]).to(self.device)
                combinedImageData[svdComponent, :, :, :] = torch.sum((im * torch.conj(coil_map)), axis=0)
                del im
            torch.cuda.empty_cache()
            return torch.moveaxis(combinedImageData, 1,-1), coil_map

    def Prep(self, rawData):
        """
        Prepare data and dependencies before reconstruction.

        Args:
            rawData (torch.Tensor): Raw k-space data with shape [numCoils, numPartitions, numReadoutPoints, numSpirals, numTimepointsPerSpiral].

        Returns:
            None
        """
        self.simulation = self.reconstructionParameters.simulation

        reconstructionMatrixSize = self.reconstructionParameters.outputMatrixSize
        if rawData.shape[1] != reconstructionMatrixSize[2]:
            numNativePartitions = rawData.shape[1]
            partitionPadWidth = int((reconstructionMatrixSize[2] - numNativePartitions)/2)
            self.rawData = torch.tensor(np.pad(rawData, ((0,0), (partitionPadWidth,partitionPadWidth), (0,0),(0,0),(0,0)))) # Potentially apply gaussian here
        else:
            self.rawData = rawData

        # Set the end of readouts along the trajectory to zero, if requested
        if self.readoutTruncationLimit > 0:
            self.rawData[:,:,self.readoutTruncationLimit:self.rawData.shape[2], :,:] = 0

        # Set up named sizes
        sizes = np.shape(self.rawData)
        self.numCoils = sizes[0]
        self.numPartitions = sizes[1]
        self.numReadoutPoints = sizes[2]
        self.numSpirals = sizes[3]
        self.numTimepointsPerSpiral = sizes[4]
        self.numSVDComponents = np.shape(self.simulation.truncationMatrix)[1]
        self.matrixSize = reconstructionMatrixSize
        self.gridSize = reconstructionMatrixSize * 2
        
        # Prepare dependencies
        self.PrepMemoryObjects()
        self.PrepNufftObjects()
        self.ktraj = self.ktraj.to(self.svdSpace.device)
        self.dcf = self.dcf.to(self.svdSpace.device)
        self.sqrt_dcf = self.sqrt_dcf.to(self.svdSpace.device)

        if(self.useDCFInIterations):
            dcfTemp = (torch.swapaxes(torch.moveaxis(self.rawData, -1, 0),-1,-2).reshape(self.numTimepointsPerSpiral, self.numCoils, self.numPartitions,-1)*self.sqrt_dcf.cpu())
            self.rawData = torch.moveaxis(torch.swapaxes(dcfTemp.reshape(self.numTimepointsPerSpiral, self.numCoils, self.numPartitions,self.numSpirals, self.numReadoutPoints),-1,-2), 0,-1)

        # Perform first pass reconstruction
        coilImageData = self.PerformThroughplaneIFFT(self.PerformAdjointNUFFTs(self.ApplySVDCompression(self.rawData), applyDCF=(self.initializeWithDCF or self.useDCFInIterations)))
        imageDataTemp, coilmapsTemp = self.PerformWalshCoilCombination(coilImageData)
        
        self.coilmaps = coilmapsTemp.to(self.images.device)
        del coilImageData, coilmapsTemp
        self.imageData = imageDataTemp.to(self.images.device)
        del imageDataTemp

        # Generate raw data mask
        self.rawDataMask = (self.rawData != 0)
        self.rawData = self.rawData[self.rawDataMask]

        # Generate image masks based on matrix size
        if self.maskingMode == "none":
            self.imageMask = torch.ones((self.numSVDComponents,self.matrixSize[0], self.matrixSize[1], self.numPartitions), dtype=bool).to(self.imageData.device)
        elif self.maskingMode == "cylindrical":
            self.imageMask = self.PrepCylindricalMask().to(self.imageData.device)
        elif self.maskingMode == "iterative_radius_spherical":
            self.imageMask = self.PrepIterativeRadiusSphericalMask().to(self.imageData.device)

    def Run(self):
        """
        Run the iterative reconstruction algorithm.

        Returns:
            tuple: A tuple containing the final image data tensor and the iteration log.
        """
        t0 = self.t0
        self.iterationLog = collections.defaultdict(list)
        self.imageData = self.imageData * self.imageMask
        g0 = self.Grad(self.imageData) * self.imageMask
        dx = -1*g0
        dxNorm = torch.norm(dx) # might be wrong norm, check torch docs
        f0, f0_l2, f0_wav = self.Objective(self.imageData ,dx, 0)
        iteration=0
        numSingleSteps=0
        restartScore = 1

        while((iteration < self.maxIterations) and (dxNorm > self.gradTolerance)): 
            self.iterationLog['f0'].append(f0.item())
            self.iterationLog['t0'].append(t0)
            self.iterationLog['dxNorm'].append(dxNorm.item())
            self.iterationLog['restartScore'].append(restartScore)            

            #live_plot(self.iterationLog, torch.abs(self.imageData[:,:,:,72].cpu()), figsize=(20,10))
            t = t0
            lsiter = 0
            while lsiter<self.maxLinesearchIterations:
                f1, f1_l2, f1_wav = self.Objective(self.imageData,dx,t)
                #print(f1, f1_l2, f1_wav)
                lsiter += 1
                #if (f1 > f0 - alpha*t*torch.abs(torch.matmul(torch.conj(g0.flatten()), dx.flatten()))**2):
                if (f1 > f0):
                    t = t * self.beta
                else:
                    break
                #else:
                #    f2 = f1
                #    steps=1
                #    while f2 < f0:
                #        steps+=1
                #        f2, f2_l2, f2_wav = self.Objective(self.imageData,dx,t*steps)
                #        print(f2, f2_l2, f2_wav)
                #    t = t * (steps-1)

            # Update timestep/learning rate
            if lsiter == 1:
                numSingleSteps+=1
                if(numSingleSteps > self.maxSingleSteps):
                    t0 = t0 / self.beta
                    numSingleSteps = 0
            else:
                t0 = t
                numSingleSteps = 0

            # Enforce max T0 
            if(t0 > self.t0Max and self.t0Max > 0):
                t0 = self.t0Max       

            # Update imageData with linesearch result (timestep*gradient)
            self.imageData = (self.imageData  + t*dx)
            f0 = f1
            g1 = self.Grad(self.imageData) * self.imageMask

            # Fletcher-Reeves
            eps = torch.finfo(torch.float32).eps
            g1_temp = g1.cpu().flatten()
            g0_temp = g0.cpu().flatten()
            bk = torch.matmul(torch.conj(g1_temp),g1_temp) / torch.matmul(torch.conj(g0_temp),(g0_temp))+eps        
            restartScore = torch.abs(torch.matmul(torch.conj(g1_temp),g0_temp)) / torch.abs(torch.matmul(torch.conj(g0_temp),g0_temp))
            if restartScore < 0.1:
                bk=0
            g0 = g1
            dx = -g1 + bk * dx
            dxNorm = torch.norm(dx)
            iteration +=1

        return self.imageData, self.iterationLog  

    def ProcessKspaceToImage(self, inputData):
        """
        Process k-space data to image data using an interative NUFFT.

        Args:
            inputData (KspaceData): Input k-space data.

        Returns:
            ImageData: Processed image data.
        """
        with torch.no_grad():
            self.Prep(inputData)
            self.Run()
            outputData = self.FinalizeResults()
            outputData = outputData.moveaxis(0,-1).unsqueeze(-1) # put into ImageData [x,y,z,t,coil] format
            return ImageData(outputData)

    @staticmethod
    def FromJson(jsonInput, reconstructionParameters, inputType, outputType):  
        """
        Create an instance of IterativeNUFFTModule from JSON input.

        Args:
            jsonInput (dict): JSON input containing module details.
            reconstructionParameters (dict): Parameters specific to the reconstruction module.
            inputType (ReconstructionModuleIOType): Input data type.
            outputType (ReconstructionModuleIOType): Output data type.

        Returns:
            IterativeNUFFTModule: Instance of IterativeNUFFTModule.
        """
        ktrajJson = jsonInput.get("ktraj")
        ktraj = torch.tensor(np.array(ktrajJson))
        dcfJson = jsonInput.get("dcf")
        dcf = torch.tensor(np.array(dcfJson))
        numNearestNeighbors = jsonInput.get("numNearestNeighbors")
        initializeWithDCF = jsonInput.get("initializeWithDCF")
        useDCFInIterations = jsonInput.get("useDCFInIterations")
        readoutTruncationLimit = jsonInput.get("readoutTruncationLimit")
        maskingMode = jsonInput.get("maskingMode")
        maxIterations = jsonInput.get("maxIterations")
        gradTolerance = jsonInput.get("gradTolerance")
        maxLinesearchIterations = jsonInput.get("maxLinesearchIterations")
        t0 = jsonInput.get("t0")
        alpha = jsonInput.get("alpha")
        beta = jsonInput.get("beta")
        maxSingleSteps = jsonInput.get("maxSingleSteps")
        t0Max = jsonInput.get("t0Max")
        waveletLambda = jsonInput.get("waveletLambda")
        waveletType = jsonInput.get("waveletType")
        waveletLevel = jsonInput.get("waveletLevel")
        device = jsonInput.get("device")

        if ktrajJson != None and dcfJson != None and numNearestNeighbors != None and device != None:
            return IterativeNUFFTModule(reconstructionParameters, inputType, outputType, ktraj, dcf, numNearestNeighbors, torch.device(device),
                                        initializeWithDCF, useDCFInIterations, readoutTruncationLimit, maskingMode, maxIterations, gradTolerance, 
                                        maxLinesearchIterations, t0, alpha, beta, maxSingleSteps, t0Max, waveletLambda, waveletLevel, waveletType)
        else:
            print("IterativeNUFFTModule requires ktraj, dcf, numNearestNeighbors, and device")