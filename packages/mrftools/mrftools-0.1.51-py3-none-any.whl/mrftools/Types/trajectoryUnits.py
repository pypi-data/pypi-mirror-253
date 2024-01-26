from .units import Units
 
class TrajectoryUnits:
    def __init__(self, gradientStrength: Units, distance:Units):
        self.gradientStrength = gradientStrength
        self.distance = distance
    
    def __dict__(self):
        unitsDict = {
            "gradientStrength":self.gradientStrength.name,
            "distance":self.distance.name
        }
        return unitsDict
    
    def __str__(self):
        return "Gradient Strength: " + str(self.gradientStrength) + " Distance: " + str(self.distance)

    @staticmethod
    def FromJson(jsonInput):  
        gradientStrengthJson = jsonInput.get("gradientStrength")
        distanceJson = jsonInput.get("distance")

        if gradientStrengthJson != None and distanceJson != None:
            return TrajectoryUnits(Units[gradientStrengthJson], Units[distanceJson])
        else:
            print("SequenceUnits requires totalDuration")

    