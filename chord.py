'''
This is a class representing a Chord.
A Chord has list of pitches (list of String),
a main pitch (String),
a mode name (String),
a suffix (String)
and a duration (Float)
'''
class Chord:
    # Constructor for Chord
    def __init__(self, main_pitch, mode_name, suffix, pitches, duration):
        self.main_pitch = main_pitch
        self.mode_name = mode_name
        self.suffix = suffix
        self.pitches = pitches
        self.duration = duration

    # Get pitches
    def getPitches(self):
        return self.pitches

    # Get duration
    def getDuration(self):
        return self.duration

    '''
    The title of a chord is a String made from
    the main pitch, the mode name, and the suffix.
    For example: A major7
    Where A is the main pitch, major is the mode, and 7 is the suffix
    indicating it is a 7th chord.
    '''
    def getTitle(self):
        return self.main_pitch + " " + self.mode_name + self.suffix