'''
This is a class for a Scale.
A Scale takes in a list of pitches (a pitch is a String),
a Mode, and a starting idx: int.
It is assumed that the starting idx is between
0 and len(notes) - 1.
'''
class Scale:
    # Constructor for Scale
    def __init__(self, pitches, mode, idx):
        self.pitches = pitches
        self.mode = mode
        self.start = idx
        self.scale = self.buildScale()

    '''
    This function returns a list of notes
    build from the full corpus of notes and
    the formula passed to this object.
    '''
    def buildScale(self):
        scale_formula = self.mode.getFormula()
        scale_length = len(scale_formula)
        note_length = len(self.pitches)
        scale = []

        index = self.start
        
        for i in range(0, scale_length):
            scale.append(self.pitches[index])
            index = (index + scale_formula[i]) % note_length 
        
        return scale

    # Getter for this Scale's scale:
    # a list of notes.
    def getScale(self):
        return self.scale

    # Returns a String that represents
    # the full title of this Scale.
    # For example: A minor
    def getTitle(self):
        return self.pitches[self.start] + " " + self.mode.getName()

'''
This is a class for a Mode.
A Mode has a name, such as 'major', 'minor', 'dorian' (A String),
and a formula (a list of Int) to produce a scale in that mode.
'''
class Mode:
    # Constructor for Mode
    def __init__(self, name, formula):
        self.name = name
        self.formula = formula

    # Get the name of this mode
    def getName(self):
        return self.name

    # Get the formula of this mode
    def getFormula(self):
        return self.formula