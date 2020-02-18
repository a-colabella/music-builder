'''
The following class represents a Time Signature.
A Time Signature has a numerator and a denomenator.
Both are assumed to be positive integers.
The denomenator is assumed to be one of 1,2,4,8,16.
'''
class TimeSignature():
    # Constructor for time signature that takes
    # in two ints
    def __init__(self, numerator, denomenator):
        self.numerator = numerator
        self.denomenator = denomenator

    # Constructor for time signature that takes
    # in a String with the following format:
    # [Numerator]/[Denomenator]
    # It is assumed to have that valid format
    def __init__(self, signature):
        split = signature.split("/")
        self.numerator = int(split[0])
        self.denomenator = int(split[1])

    # Get numerator
    def getNumerator(self):
        return self.numerator

    # Get denomenator
    def getDenomenator(self):
        return self.denomenator

    # Duration in float
    def getDuration(self):
        return (float(self.numerator) / float(self.denomenator))
    
