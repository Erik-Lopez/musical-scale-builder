NOTE_AMOUNT = 12
NOTES_ES_SHARP = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]
NOTES_ES_FLAT = ["Do", "Re♭", "Re", "Mi♭", "Mi", "Fa", "Sol♭", "Sol", "La♭", "La", "Si♭", "Si"]
NOTES_EN_SHARP = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
NOTES_EN_FLAT = ["C", "D♭", "D", "E♭", "E", "F", "G♭", "G", "A♭", "A", "B♭", "B"]

note_lists = {
        "sostenidos": NOTES_ES_SHARP,
        "bemoles": NOTES_ES_FLAT,
        "flats": NOTES_EN_FLAT,
        "sharps": NOTES_EN_SHARP
}

print("NOMENCLATURA")
for option in note_lists.keys():
    print("\t- %s" % option)

note_list = note_lists[input("Selecciona entre las opciones anteriores: ").lower()]

### MODES ###
T = 2
sT = 1
MAJOR_MODE      = [T, T, sT, T, T, T, sT]
DORIAN_MODE     = [T, sT, T, T, T, sT, T]
FRIGIAN_MODE    = [sT, T, T, T, sT, T, T]
LIDIAN_MODE     = [T, T, T, sT, T, T, sT]
MIXOLIDIAN_MODE = [T, T, sT, T, T, sT, T]
EOLIAN_MODE     = [T, sT, T, T, sT, T, T]
LOCRIAN_MODE    = [sT, T, T, sT, T, T, T]

NOTE_NAME_TO_INDEX = {
        note_list[i]: i for i in range(0, 12)
}

def simplify_note_index(index):
    return index - (index // NOTE_AMOUNT)*NOTE_AMOUNT

class Note:
    index_from_c: int

    def __init__(self, name):
        self.index_from_c = NOTE_NAME_TO_INDEX[name]

    def get_index_scale(self, mode: list):
        index_scale = [self.index_from_c]

        for interval in mode:
            raw_index = index_scale[-1] + interval
            simplified_index = simplify_note_index(raw_index)

            index_scale.append(simplified_index)
        
        return index_scale

    def get_name_scale(self, mode: list, note_list: list):
        index_scale = self.get_index_scale(mode)
        name_scale = []

        for index in index_scale:
            name_scale.append(note_list[index])

        return name_scale

    def get_note_scale(self, mode: list):
        index_scale = self.get_index_scale(mode)
        note_scale = []
        for index in index_scale:
            note = Note(index)
            note_scale.append(note)

modes = {
        "jonico": MAJOR_MODE, 
        "dorico": DORIAN_MODE, 
        "frigio": FRIGIAN_MODE, 
        "lidio": LIDIAN_MODE, 
        "mixolidio": MIXOLIDIAN_MODE,
        "eolico": EOLIAN_MODE, 
        "locrio": LOCRIAN_MODE, 
}

name = input("Introduce tu nota: ")
note = Note(name=name)

print("MODOS")
for option in modes.keys():
    print("\t- %s" % option)

mode = input("Selecciona entre las opciones anteriores: ").lower()

scale = note.get_name_scale(modes[mode], note_list)

print("\n¡Aquí tienes tu escala!")

for note in scale:
    print("  %s" % note, end="")

print("\n")
