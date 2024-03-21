from functools import total_ordering


long_notes = {"до": "до-о", "ре": "ре-э", "ми": "ми-и", "фа": "фа-а",
              "соль": "со-оль", "ля": "ля-а", "си": "си-и"}
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
N = 7
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


@total_ordering
class Note:
    def __init__(self, note, is_long=False):
        self.pitch = note
        self.is_long = is_long

    def __str__(self):
        if self.is_long:
            return long_notes[self.pitch]
        return self.pitch

    def __lt__(self, other):
        return PITCHES.index(self.pitch) < PITCHES.index(other.pitch)

    def __eq__(self, other):
        return self.pitch == other.pitch

    def __rshift__(self, num):
        ind = (self.get_index() + num) % N
        return Note(PITCHES[ind], self.is_long)

    def __lshift__(self, num):
        ind = (self.get_index() - num) % N
        return Note(PITCHES[ind], self.is_long)

    def get_index(self):
        return PITCHES.index(self.pitch)

    def get_interval(self, other):
        dif = abs(self.get_index() - PITCHES.index(other.pitch))
        return INTERVALS[dif]