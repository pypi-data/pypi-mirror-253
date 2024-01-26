import mrftools.Utilities.twixtools as twixtools
import numpy as np
from tqdm import tqdm
from enum import Enum, IntEnum
import scipy.io
import ismrmrd

class FAMode(Enum):
    RequestedFlipAngle = 1
    ReportedFlipAngle = 2

class mrftoolsIceProgramPara(IntEnum):
    timepoint = 0
    undersampledPartition = 1
    tr = 2
    te = 3
    fa_requested = 4
    fa_reported = 5
    ph = 6

class mrftoolsDataset:
    def __init__(self):
        self.sourceFilename = None
        self.faMode = None
        self.numSpirals = None
        self.numMeasuredPartitions = None
        self.numUndersampledPartitions = None
        self.centerMeasuredPartition = None
        self.numSets = None
        self.numCoils = None
        self.matrixSize = None
        self.FOV = None
        self.ismrmrdHeader = None
        self.undersamplingRatio = None
        self.numTimepoints = None
        self.TRs = None
        self.TEs = None
        self.FAs = None
        self.PHs = None
        self.IDs = None
        self.rawData = None
        self.acqHeaders = None
        self.discardPre = None
        self.discardPost = None
        self.numReadoutPoints = None
        self.usePartialFourier = None
        self.partialFourierRatio = None
        self.sequence = None
        self.sequenceType = None
        self.sequenceHash = None

    def __str__(self):
        descriptionString = f""" 
        Source Filename: {self.sourceFilename} 
        Matrix Size: {self.matrixSize} ({self.numUndersampledPartitions} w/ {self.undersamplingRatio}x undersampling)
        Partial Fourier: {self.partialFourierRatio}
        FOV: {self.FOV}
        Timepoints: {self.numTimepoints} ({self.numSpirals} spirals x {self.numSets} sets)
        Coils: {self.numCoils}
        Raw Data Size: {np.shape(self.rawData)}
        Sequence:
            Hash: {self.sequenceHash}
            TRs: {np.min(self.TRs)}, {np.max(self.TRs)}
            TEs: {np.min(self.TEs)}, {np.max(self.TEs)}
            FAs: {np.min(self.FAs)}, {np.max(self.FAs)}
            PHs: {np.min(self.PHs)}, {np.max(self.PHs)}
            IDs: {np.min(self.IDs)}, {np.max(self.IDs)}
        """
        return descriptionString

    def PopulateIsmrmrdHeader(mdb):
        acqHeader = ismrmrd.Acquisition()
        acqHeader.position[0] = mdb.mdh.SliceData.SlicePos.Sag
        acqHeader.position[1] = mdb.mdh.SliceData.SlicePos.Cor
        acqHeader.position[2] = mdb.mdh.SliceData.SlicePos.Tra
        quat = mdb.mdh.SliceData.Quaternion
        a = quat[0]; b = quat[1]; c = quat[2]; d = quat[3]
        acqHeader.read_dir[0] = 1.0 - 2.0 * (b * b + c * c)
        acqHeader.phase_dir[0] = 2.0 * (a * b - c * d)
        acqHeader.slice_dir[0] = 2.0 * (a * c + b * d)
        acqHeader.read_dir[1] = 2.0 * (a * b + c * d)
        acqHeader.phase_dir[1] = 1.0 - 2.0 * (a * a + c * c)
        acqHeader.slice_dir[1] = 2.0 * (b * c - a * d)
        acqHeader.read_dir[2] = 2.0 * (a * c - b * d)
        acqHeader.phase_dir[2] = 2.0 * (b * c + a * d)
        acqHeader.slice_dir[2] = 1.0 - 2.0 * (a * a + b * b)
        return acqHeader

    def InitializeFromTwix(filename, multi_twix, trajectoryReadoutLength=-1, fa_mode='requested'):
        dataset = mrftoolsDataset()
        dataset.sourceFilename = filename
        dataset.trajectoryReadoutLength = trajectoryReadoutLength
        if fa_mode == 'requested':
            dataset.faMode = FAMode.RequestedFlipAngle
        elif fa_mode == 'reported':
            dataset.faMode = FAMode.ReportedFlipAngle
        dataset.numSpirals = int(multi_twix[-1]['hdr']['Meas']['iNoOfFourierLines']); 
        dataset.numMeasuredPartitions = int(multi_twix[-1]['hdr']['Meas']['iNoOfFourierPartitions']); 
        dataset.numUndersampledPartitions = int(multi_twix[-1]['hdr']['MeasYaps']['sKSpace']['lPartitions']); 
        dataset.centerMeasuredPartition =  int(dataset.numMeasuredPartitions/2);  # Fix this to work with partial fourier
        dataset.numSets = int(multi_twix[-1]['hdr']['Meas']['iNSet']); 
        dataset.numCoils = int(multi_twix[-1]['hdr']['Meas']['iMaxNoOfRxChannels']); 
        xMatSize = multi_twix[-1]['hdr']['MeasYaps']['sKSpace']['lBaseResolution']
        yMatSize = multi_twix[-1]['hdr']['MeasYaps']['sKSpace']['lPhaseEncodingLines']
        zMatSize = multi_twix[-1]['hdr']['MeasYaps']['sKSpace']['lImagesPerSlab']
        dataset.matrixSize = np.array([xMatSize, yMatSize, zMatSize]); 
        xFOV = multi_twix[-1]['hdr']['MeasYaps']['sSliceArray']['asSlice'][0]['dReadoutFOV']
        yFOV = multi_twix[-1]['hdr']['MeasYaps']['sSliceArray']['asSlice'][0]['dPhaseFOV']
        zFOV = multi_twix[-1]['hdr']['MeasYaps']['sSliceArray']['asSlice'][0]['dThickness']
        dataset.FOV = np.array([xFOV, yFOV, zFOV])
        dataset.undersamplingRatio = 1
        if(dataset.numUndersampledPartitions > 1): # May not work for multislice 2d
            dataset.undersamplingRatio = int(dataset.numUndersampledPartitions / (dataset.centerMeasuredPartition * 2)); 
        dataset.usePartialFourier = False
        if(dataset.numMeasuredPartitions*dataset.undersamplingRatio < dataset.numUndersampledPartitions):
            dataset.usePartialFourier = True
            dataset.partialFourierRatio = dataset.numMeasuredPartitions / (dataset.numUndersampledPartitions/dataset.undersamplingRatio)
            print(f'Measured partitions is less than expected for undersampling ratio - assuming partial fourier acquisition with ratio: {dataset.partialFourierRatio}')

        # Set up sequence parameter arrays
        dataset.numTimepoints = dataset.numSets*dataset.numSpirals
        dataset.TRs = np.zeros((dataset.numTimepoints, dataset.numMeasuredPartitions))
        dataset.TEs = np.zeros((dataset.numTimepoints, dataset.numMeasuredPartitions))
        dataset.FAs = np.zeros((dataset.numTimepoints, dataset.numMeasuredPartitions))
        dataset.PHs = np.zeros((dataset.numTimepoints, dataset.numMeasuredPartitions))
        dataset.IDs = np.zeros((dataset.numTimepoints, dataset.numMeasuredPartitions))

        # Set up raw data and header arrays
        dataset.ismrmrdHeader = ismrmrd.xsd.ismrmrdHeader()
        matrixSizeHeader=ismrmrd.xsd.matrixSizeType(xMatSize, yMatSize, zMatSize)
        fovHeader=ismrmrd.xsd.fieldOfViewMm(xFOV, yFOV, zFOV)
        encoding = ismrmrd.xsd.encodingType(reconSpace=ismrmrd.xsd.encodingSpaceType(matrixSize=matrixSizeHeader, fieldOfView_mm=fovHeader))
        dataset.ismrmrdHeader.encoding.append(encoding)
        dataset.acqHeaders = np.empty((dataset.numUndersampledPartitions, dataset.numSpirals, dataset.numSets), dtype=ismrmrd.Acquisition)

        # Process data as it comes in
        print("Reading headers and populating dataset:")
        with tqdm(total=len(multi_twix[-1]['mdb'])) as pbar:
            for mdb in multi_twix[-1]['mdb']:
                if mdb is None:
                    pbar.update(1)
                    break
                if mdb.is_flag_set('NOISEADJSCAN') or mdb.is_flag_set('PHASCOR'):
                    pbar.update(1)
                    continue
                else:
                    dataset.TRs[mdb.mdh.IceProgramPara[mrftoolsIceProgramPara.timepoint], mdb.mdh.Counter.Par] = mdb.mdh.IceProgramPara[mrftoolsIceProgramPara.tr]          
                    dataset.TEs[mdb.mdh.IceProgramPara[mrftoolsIceProgramPara.timepoint], mdb.mdh.Counter.Par] = mdb.mdh.IceProgramPara[mrftoolsIceProgramPara.te]
                    if dataset.faMode==FAMode.RequestedFlipAngle:
                        dataset.FAs[mdb.mdh.IceProgramPara[mrftoolsIceProgramPara.timepoint], mdb.mdh.Counter.Par] = mdb.mdh.IceProgramPara[mrftoolsIceProgramPara.fa_requested]  # Use requested Flip Angle
                    elif dataset.faMode==FAMode.ReportedFlipAngel:
                        dataset.FAs[mdb.mdh.IceProgramPara[mrftoolsIceProgramPara.timepoint], mdb.mdh.Counter.Par] = mdb.mdh.IceProgramPara[mrftoolsIceProgramPara.fa_reported]  # Use reported Flip Angle
                    dataset.PHs[mdb.mdh.IceProgramPara[mrftoolsIceProgramPara.timepoint], mdb.mdh.Counter.Par] = mdb.mdh.IceProgramPara[mrftoolsIceProgramPara.ph] 
                    dataset.IDs[mdb.mdh.IceProgramPara[mrftoolsIceProgramPara.timepoint], mdb.mdh.Counter.Par] = mdb.mdh.Counter.Lin
                    dataset.acqHeaders[mdb.mdh.IceProgramPara[mrftoolsIceProgramPara.undersampledPartition], mdb.mdh.Counter.Lin, mdb.mdh.Counter.Set] = mrftoolsDataset.PopulateIsmrmrdHeader(mdb) # [undersampledPartition, spiralID, set]
                    if dataset.rawData is None:
                        dataset.discardPre = int(mdb.mdh.CutOff.Pre / 2); # Fix doubling in sequence - weird; I think this is because of the sequence parameter "RO Oversample" in the rseqlim
                        if(dataset.trajectoryReadoutLength != -1):
                            dataset.discardPost = dataset.discardPre + dataset.trajectoryReadoutLength; # Fix in sequence
                        else:                             
                            dataset.discardPost = mdb.data.shape[1]
                        dataset.numReadoutPoints = dataset.discardPost-dataset.discardPre; 
                        dataset.rawData = np.zeros([dataset.numCoils, dataset.numUndersampledPartitions, dataset.numReadoutPoints, dataset.numSpirals, dataset.numSets], dtype=np.complex64)
                    dataset.rawData[:, mdb.mdh.IceProgramPara[mrftoolsIceProgramPara.undersampledPartition], :, mdb.mdh.Counter.Lin, mdb.mdh.Counter.Set] = mdb.data[:, dataset.discardPre:dataset.discardPost]
                    pbar.update(1)

        # Setup sequence parameter definition
        #dataset.sequenceType = SequenceType.FISP # This is hard coded to FISP - need a flag in the dat file!
        #dataset.sequence = SequenceParameters("from_twix_header", dataset.sequenceType) 
        #dataset.sequence.Initialize(dataset.TRs[:,0]/(1000*1000), dataset.TEs[:,0]/(1000*1000), dataset.FAs[:,0]/(100), dataset.PHs[:,0]/(100), dataset.IDs[:,0])
        #dataset.sequenceHash = hashlib.sha256(pickle.dumps(dataset.sequence)).hexdigest()

        #dictionary = None
        #simulation = None

        return dataset #, dictionary, simulation

    def InitializeFromLegacyTwix(filename, multi_twix, legacy_settings, trajectoryReadoutLength):
        dataset = mrftoolsDataset()
        dataset.sourceFilename = filename
        dataset.trajectoryReadoutLength = trajectoryReadoutLength
        dataset.faMode = FAMode.RequestedFlipAngle
        dataset.numSpirals = 48
        dataset.numMeasuredPartitions = 40
        dataset.numUndersampledPartitions = 120
        dataset.centerMeasuredPartition =  int(dataset.numMeasuredPartitions/2)
        dataset.numSets = 10
        dataset.numCoils = int(multi_twix[-1]['hdr']['Meas']['iMaxNoOfRxChannels']); 
        xMatSize = multi_twix[-1]['hdr']['MeasYaps']['sKSpace']['lBaseResolution']
        yMatSize = multi_twix[-1]['hdr']['MeasYaps']['sKSpace']['lPhaseEncodingLines']
        zMatSize = multi_twix[-1]['hdr']['MeasYaps']['sKSpace']['lImagesPerSlab']
        dataset.matrixSize = np.array([xMatSize, yMatSize, zMatSize]); 
        xFOV = multi_twix[-1]['hdr']['MeasYaps']['sSliceArray']['asSlice'][0]['dReadoutFOV']
        yFOV = multi_twix[-1]['hdr']['MeasYaps']['sSliceArray']['asSlice'][0]['dPhaseFOV']
        zFOV = multi_twix[-1]['hdr']['MeasYaps']['sSliceArray']['asSlice'][0]['dThickness']
        dataset.FOV = np.array([xFOV, yFOV, zFOV])
        dataset.undersamplingRatio = 3
        dataset.usePartialFourier = False

        dataset.numTimepoints = dataset.numSets*dataset.numSpirals

        # Load text and bin files
        USID = scipy.io.loadmat(legacy_settings.dependencyDirectory + legacy_settings.usidFile)

        # Set up sequence parameter arrays
        dataset.numTimepoints = dataset.numSets*dataset.numSpirals
        dataset.TRs = np.ones((dataset.numTimepoints, dataset.numMeasuredPartitions)) * legacy_settings.baseTR + np.swapaxes((np.tile(np.loadtxt(legacy_settings.dependencyDirectory + legacy_settings.trFile)[0:dataset.numTimepoints],dataset.numMeasuredPartitions)).reshape([dataset.numMeasuredPartitions,-1]),0,1)
        dataset.TEs = np.ones((dataset.numTimepoints, dataset.numMeasuredPartitions)) * legacy_settings.baseTE 
        dataset.FAs = np.swapaxes((np.tile(np.loadtxt(legacy_settings.dependencyDirectory + legacy_settings.faFile)[0:dataset.numTimepoints],dataset.numMeasuredPartitions)).reshape([dataset.numMeasuredPartitions,-1]),0,1) * legacy_settings.faScaling
        dataset.PHs = np.swapaxes((np.tile(np.loadtxt(legacy_settings.dependencyDirectory + legacy_settings.phFile)[0:dataset.numTimepoints],dataset.numMeasuredPartitions)).reshape([dataset.numMeasuredPartitions,-1]),0,1)
        dataset.IDs = np.swapaxes((np.tile(np.loadtxt(legacy_settings.dependencyDirectory + legacy_settings.idFile)[0:dataset.numTimepoints],dataset.numMeasuredPartitions)).reshape([dataset.numMeasuredPartitions,-1]),0,1)

        # Set up raw data and header arrays
        dataset.ismrmrdHeader = ismrmrd.xsd.ismrmrdHeader()
        matrixSizeHeader=ismrmrd.xsd.matrixSizeType(xMatSize, yMatSize, zMatSize)
        fovHeader = ismrmrd.xsd.fieldOfViewMm(xFOV, yFOV, zFOV)
        encoding = ismrmrd.xsd.encodingType(reconSpace=ismrmrd.xsd.encodingSpaceType(matrixSize=matrixSizeHeader, fieldOfView_mm=fovHeader))
        dataset.ismrmrdHeader.encoding.append(encoding)
        dataset.acqHeaders = np.empty((dataset.numUndersampledPartitions, dataset.numSpirals, dataset.numSets), dtype=ismrmrd.Acquisition)

        # Process data as it comes in
        print("Reading headers and populating dataset:")
        with tqdm(total=len(multi_twix[-1]['mdb'])) as pbar:
            for mdb in multi_twix[-1]['mdb']:
                if mdb is None:
                    pbar.update(1)
                    break
                if mdb.is_flag_set('NOISEADJSCAN') or mdb.is_flag_set('PHASCOR'):
                    pbar.update(1)
                    continue
                else:
                    timepoint = mdb.mdh.Counter.Set
                    undersampledPartition = mdb.mdh.Counter.Par
                    currentSpiral = int(timepoint%dataset.numSpirals)
                    currentSet = int(timepoint/dataset.numSpirals)
                    dataset.acqHeaders[undersampledPartition, currentSpiral, currentSet] = mrftoolsDataset.PopulateIsmrmrdHeader(mdb) # [undersampledPartition, spiralID, set]
                    if dataset.rawData is None:
                        dataset.discardPre = 20; # Fix doubling in sequence - weird; I think this is because of the sequence parameter "RO Oversample" in the rseqlim
                        if(dataset.trajectoryReadoutLength != -1):
                            dataset.discardPost = dataset.discardPre + dataset.trajectoryReadoutLength; # Fix in sequence
                        else:                             
                            dataset.discardPost = mdb.data.shape[1]
                        dataset.numReadoutPoints = dataset.discardPost-dataset.discardPre; 
                        dataset.rawData = np.zeros([dataset.numCoils, dataset.numUndersampledPartitions, dataset.numReadoutPoints, dataset.numSpirals, dataset.numSets], dtype=np.complex64)
                    dataset.rawData[:, undersampledPartition, :, currentSpiral, currentSet] = mdb.data[:, dataset.discardPre:dataset.discardPost]
                    pbar.update(1)

        # Setup sequence parameter definition
        #dataset.sequenceType = SequenceType.FISP # This is hard coded to FISP - need a flag in the dat file!
        #dataset.sequence = SequenceParameters("from_twix_header", dataset.sequenceType) 
        #dataset.sequence.Initialize(dataset.TRs[:,0]/(1000*1000), dataset.TEs[:,0]/(1000*1000), dataset.FAs[:,0], dataset.PHs[:,0], dataset.IDs[:,0])
        #dataset.sequenceHash = hashlib.sha256(pickle.dumps(dataset.sequence)).hexdigest()

        # Initialize Dictionary
        #f = h5py.File(datasetSettings.legacy_settings.dependencyDirectory + datasetSettings.legacy_settings.dictionaryFile)
        #T1s=f['Dsvd']['r'][0,:]/1000
        #T2s=f['Dsvd']['r'][1,:]/1000
        #B1s=f['Dsvd']['dB1_all'][:,0]
        #truncationNumber = f['Dsvd']['Nk'][0]
        #dictionary = DictionaryParameters("fromMatlab")
        #dictionary.Initialize(T1s, T2s)

        # Initialize Simulation from dataset and dictionary
        #simulation = Simulation(dataset.sequence, dictionary, phaseRange=(-1*np.pi, 1*np.pi), numSpins=200)
        #simulation.singularValues = f['Dsvd']['singvals'][0,:]
        #simulation.truncatedResults = np.transpose(f['Dsvd']['Dtrunc'][:])
        #simulation.truncatedResults = simulation.truncatedResults['real']+simulation.truncatedResults['imag']*1j
        #simulation.truncationMatrix = np.transpose(f['Dsvd']['Vtrunc'][:])
        #simulation.truncationMatrix = simulation.truncationMatrix['real']+simulation.truncationMatrix['imag']*1j
        #dictionary = None
        #simulation = None

        return dataset #, dictionary, simulation
    
    def Initialize(filename, trajectoryReadoutLength=-1, fa_mode='requested', legacy_settings = None):
        multi_twix = twixtools.read_twix(filename)
        protocolName = multi_twix[1]['hdr']['Config']['SequenceFileName']
        if 'dmMRF_3Dslab_EXUVA' in  protocolName:
            return mrftoolsDataset.InitializeFromLegacyTwix(filename, multi_twix, legacy_settings, trajectoryReadoutLength) 
        else:
            return mrftoolsDataset.InitializeFromTwix(filename, multi_twix, trajectoryReadoutLength, fa_mode)
