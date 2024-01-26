from .units import Units
 
class SequenceUnits:
    def __init__(self, time:Units, angle:Units):
        self.time = time
        self.angle = angle
    
    def __dict__(self):
        unitsDict = {
            "time":self.time.name,
            "angle":self.angle.name
        }
        return unitsDict
    
    def __str__(self):
        return "Time: " + str(self.time) + " Angle: " + str(self.angle)

    @staticmethod
    def FromJson(jsonInput):  
        timeJson = jsonInput.get("time")
        angleJson = jsonInput.get("angle")

        if timeJson != None and angleJson != None:
            return SequenceUnits(Units[timeJson], Units[angleJson])
        else:
            print("SequenceUnits requires totalDuration")

    