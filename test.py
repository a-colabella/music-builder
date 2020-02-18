import note, chord, scale, measure, time_signature

corpus = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
key = 5
formula = [2,2,1,2,2,2,1]
name = "major"

min_duration = 0.0625
max_duration = 1

mode = scale.Mode(name, formula)
scale = scale.Scale(corpus, mode, key)

print(scale.getTitle())
print(scale.getScale())

nb = note.NoteBuilder(scale, min_duration, max_duration)

for i in range(0, 7):
    n = nb.newNote()
    print(n.getPitch() + " " + str(n.getDuration()))

print("--------")

tim = time_signature.TimeSignature("4/4")

print(tim.getDuration())

mb = measure.MeasureBuilder(tim, scale, min_duration, max_duration)

m = mb.newMeasure()

for x in m.getNotes():
    print(x.getPitch() + " " + str(x.getDuration()))