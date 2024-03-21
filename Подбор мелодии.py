N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, nota, is_long=False):
        self.is_long = is_long
        self.tone = PITCHES.index(nota)

    def __str__(self):
        return PITCHES[self.tone] if not self.is_long else LONG_PITCHES[self.tone]

    def __repr__(self):
        return PITCHES[self.tone] if not self.is_long else LONG_PITCHES[self.tone]

    def __gt__(self, other):
        return self.tone > other.tone

    def __lt__(self, other):
        return self.tone < other.tone

    def __ge__(self, other):
        return self.tone >= other.tone

    def __le__(self, other):
        return self.tone <= other.tone

    def __eq__(self, other):
        return self.tone == other.tone

    def __ne__(self, other):
        return self.tone != other.tone

    def __rshift__(self, other):
        step = (self.tone + other) - ((self.tone + other) // N) * N
        return Note(step + self.tone, self.is_long)

    def __lshift__(self, other):
        new_tone = self.tone - other
        while new_tone < 0:
            new_tone += N
        return Note(new_tone, self.is_long)

    def get_interval(self, other):
        return INTERVALS[abs(other.tone - self.tone)]

    def tone(self):
        return self.tone

    def is_long(self):
        return self.is_long


class Melody:
    def __init__(self, melody=[]):
        self.melody = melody.copy()

    def __str__(self):
        return ', '.join(map(str, self.melody)).capitalize()

    def append(self, obj):
        self.melody.append(obj)

    def replace_last(self, obj):
        self.melody[-1] = obj

    def remove_last(self):
        del self.melody[-1]

    def clear(self):
        self.melody.clear()

    def __len__(self):
        return len(self.melody)

    def __rshift__(self, num):
        if all([elem.tone + num < N for elem in self.melody]):
            new_melody = Melody()
            for elem in self.melody:
                new_melody.append(Note(PITCHES[elem.tone + num], elem.is_long))
            return new_melody
        else:
            new_melody = Melody()
            for elem in self.melody:
                new_melody.append(Note(PITCHES[elem.tone], elem.is_long))
            return new_melody

    def __lshift__(self, num):
        if all([elem.tone - num >= 0 for elem in self.melody]):
            new_melody = Melody()
            for elem in self.melody:
                new_melody.append(Note(PITCHES[elem.tone - num], elem.is_long))
            return new_melody
        else:
            new_melody = Melody()
            for elem in self.melody:
                new_melody.append(Note(PITCHES[elem.tone], elem.is_long))
            return new_melody