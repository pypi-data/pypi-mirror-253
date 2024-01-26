from .types import ReconstructionModuleIOType
import torch 

class DataStruct():
    def __init__(self):
        self.data = None
        self.dataType = None
    def __str__(self) -> str:
        return str(self.dataType) + str(self.data)

# [coil, partition, readout, spiral, spiralTimepoint]
class KspaceData(DataStruct):
    def __init__(self, data):
        if torch.is_tensor(data):
            self.data = data
        else: 
            self.data = torch.tensor(data)
        self.dataType = ReconstructionModuleIOType.KSPACE

# [x, y, z, t, coil]
class ImageData(DataStruct):
    def __init__(self, data):
        if torch.is_tensor(data):
            self.data = data
        else: 
            self.data = torch.tensor(data)
        self.dataType = ReconstructionModuleIOType.IMAGE

# [x,y,z]
class MapData(DataStruct):
    def __init__(self, data):
        self.data = data
        self.dataType = ReconstructionModuleIOType.MAP
