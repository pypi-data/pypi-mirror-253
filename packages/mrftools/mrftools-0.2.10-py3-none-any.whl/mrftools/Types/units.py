from enum import Enum

class Units(Enum):
    SECONDS = 0
    MILLISECONDS = 1
    MICROSECONDS = 2
    DEGREES = 3
    CENTIDEGREES = 4
    RADIANS = 5
    CENTIRADIANS = 6
    METERS = 7
    CENTIMETERS = 8
    MILLIMETERS = 9
    MILLITESLA_PER_METER = 10 

    @staticmethod
    def Convert(input, inputUnits, outputUnits):
        if(inputUnits == Units.SECONDS):
            if(outputUnits == Units.SECONDS):
                return input
            if(outputUnits == Units.MILLISECONDS):
                return input*1000
            if(outputUnits == Units.MICROSECONDS):
                return input*(1000*1000)
            else:
                print("Cannot convert", inputUnits, "to", outputUnits)
                return None
        if(inputUnits == Units.MILLISECONDS):
            if(outputUnits == Units.SECONDS):
                return input/1000
            if(outputUnits == Units.MILLISECONDS):
                return input
            if(outputUnits == Units.MICROSECONDS):
                return input*1000
            else:
                print("Cannot convert", inputUnits, "to", outputUnits)
                return None
        if(inputUnits == Units.MICROSECONDS):
            if(outputUnits == Units.SECONDS):
                return input/(1000*1000)
            if(outputUnits == Units.MILLISECONDS):
                return input/1000
            if(outputUnits == Units.MICROSECONDS):
                return input
            else:
                print("Cannot convert", inputUnits, "to", outputUnits)
                return None
        if(inputUnits == Units.DEGREES):
            if(outputUnits == Units.DEGREES):
                return input
            if(outputUnits == Units.CENTIDEGREES):
                return input*100
            if(outputUnits == Units.RADIANS):
                return (input/180)*np.pi
            if(outputUnits == Units.CENTIRADIANS):
                return (input/180)*np.pi * 100
            else:
                print("Cannot convert", inputUnits, "to", outputUnits)
                return None
        if(inputUnits == Units.CENTIDEGREES):
            if(outputUnits == Units.DEGREES):
                return input/100
            if(outputUnits == Units.CENTIDEGREES):
                return input
            if(outputUnits == Units.RADIANS):
                return (input/100/180)*np.pi
            if(outputUnits == Units.CENTIRADIANS):
                return (input/180)*np.pi
            else:
                print("Cannot convert", inputUnits, "to", outputUnits)
                return None
        if(inputUnits == Units.RADIANS):
            if(outputUnits == Units.DEGREES):
                return (input/np.pi)*180
            if(outputUnits == Units.CENTIDEGREES):
                return (input/np.pi)*180*100
            if(outputUnits == Units.RADIANS):
                return input
            if(outputUnits == Units.CENTIRADIANS):
                return input*100
            else:
                print("Cannot convert", inputUnits, "to", outputUnits)
                return None
        if(inputUnits == Units.CENTIRADIANS):
            if(outputUnits == Units.DEGREES):
                return (input/100/np.pi)*180
            if(outputUnits == Units.CENTIDEGREES):
                return (input/np.pi)*180
            if(outputUnits == Units.RADIANS):
                return input/100
            if(outputUnits == Units.CENTIRADIANS):
                return input
            else:
                print("Cannot convert", inputUnits, "to", outputUnits)
                return None
        else:
            print("Cannot convert", inputUnits, "to", outputUnits)
            return None 