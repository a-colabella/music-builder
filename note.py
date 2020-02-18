import random, scale, utils

ABSOLUTE_MIN_DURATION = 0.0625

'''
This is a class representing a Note.
A Note has a pitch (String) and a duration (Float)
'''
class Note:
    # Constructor for note
    def __init__(self, pitch, duration):
        self.pitch = pitch
        self.duration = duration

    # Gets the pitch
    def getPitch(self):
        return self.pitch

    # Gets the duration
    def getDuration(self):
        return self.duration

'''
This class represents a NoteBuilder.
It takes in a Scale, min_duration (float), max_duration (float).
It can create a random note within a Scale and following
the duration rules provided.
It is assumed that min_duration < max_duration
'''
class NoteBuilder:
    # Constructor for NoteBuilder
    def __init__(self, scale, min_duration, max_duration):
        self.scale = scale
        self.min_duration = min_duration
        self.max_duration = max_duration

    # Gets a random pitch from a Scale
    def randomPitch(self):
        return random.choice(self.scale.getScale())

    # Gets a random duration within the min and max
    def randomDuration(self):
        r = list(utils.floatrange(self.min_duration, self.max_duration, ABSOLUTE_MIN_DURATION))

        return random.choice(r)

    # Returns a new random note
    def newNote(self):
        pitch = self.randomPitch()
        duration = self.randomDuration()
        return Note(pitch, duration)