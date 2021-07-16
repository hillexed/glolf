ratings = [
"Everyone",
"Teen",
"Everyone 10+",
"Good",
"Acceptable",
"Marginal",
"Poor",
]


scaleTypes = [
"Major",
"Harmonic Minor",
"Minor",
"Pentatonic",
"Dorian",
"Phrygian",
"Lydian",
"Mixolydian",
"Locrian", # sure i'll take it
"Whole-Tone",
"Blues Scale",
"Acoustic",
]

startingNotes = [
"C",
"C#"
"D"
"D#"
"E"
"F"
"F#"
"G"
"G#"
"A"
"A#"
"B"
]

scales = []

for startingNote in startingNotes:
    for scaleType in scaleTypes:
        scales.append(f"{startingNote} {scaleType}")
