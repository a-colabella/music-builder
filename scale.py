'''
This is a class for a Scale.
A Scale takes in a list of notes (a note is a String),
a formula: List of int,
and a starting idx: int.
It is assumed that the starting idx is between
0 and len(notes) - 1.
'''
class Scale:
    '''
    This function returns a list of notes
    build from the full corpus of notes and
    the formula passed to this object.
    '''
    def buildScale(self):
        scale_length = len(self.formula)
        note_length = len(self.notes)
        scale = []

        index = self.start
        
        for i in range(0, scale_length):
            scale.append(self.notes[index])
            index = (index + self.formula[i]) % note_length 
        
        return scale

    # Constructor for Scale
    def __init__(self, notes, formula, idx):
        self.notes = notes
        self.formula = formula
        self.start = idx
        self.scale = self.buildScale()

    # Getter for this Scale's scale:
    # a list of notes.
    def getScale(self):
        return self.scale