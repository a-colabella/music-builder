import time_signature, note

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

'''
This class represents a MeasureBuilder.
A MeasureBuilder takes in a time_signature, a scale, a
min_note_duration, and a max_note_duration.
And can construct a scale within that time_signature and scale
using a NoteBuilder.
'''
class MeasureBuilder:
    # Constructor for measure builder
    def __init__(self, time_signature, scale, min_note_duration, max_note_duration):
        self.time_signature = time_signature
        self.scale = scale
        self.min_note_duration = min_note_duration
        self.max_note_duration = max_note_duration

    # Returns a new random measure
    def newMeasure(self):
        # Initialize a NoteBuilder
        nb = note.NoteBuilder(self.scale, self.min_note_duration, self.max_note_duration)

        # Initialize combined_duration which ensures
        # the sum of each note duration is below the 
        # time signature duration
        combined_duration = 0.0
        max_duration = self.time_signature.getDuration()
        notes = []

        # Generate new random notes
        while(combined_duration < max_duration):
            n = nb.newNote()
            combined_duration = combined_duration + n.getDuration()

            if (combined_duration > max_duration):
                break
            
            notes.append(n)
            
        return Measure(self.time_signature, notes)
        