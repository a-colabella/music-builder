import time_signature

'''
This class represents a Measure.
A Measure has a time signature and a list of Notes.
It is assumed that the sum of the durations of the Notes are
less than or equal to the duration of the time signature.
'''
class Measure:
    # Constructor for measure
    def __init__(self, time_signature, notes):
        self.time_signature = time_signature
        self.notes = notes

    # Getter for Notes
    def getNotes(self):
        return self.notes

    # Getter for Time Signature
    def getTimeSignature(self):
        return self.time_signature