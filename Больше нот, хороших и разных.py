long = {'до': 'до-о',
        'ре': 'ре-э',
        'ми': 'ми-и',
        'фа': 'фа-а',
        'соль': 'со-оль',
        'ля': 'ля-а',
        'си': 'си-и'}
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    def __init__(self, pitch, is_long=False):
        self.pitch = pitch
        self.is_long = is_long

    def __str__(self):
        if self.is_long:
            return long[self.pitch]
        return self.pitch


class LoudNote(Note):
    def __str__(self):
        return super().__str__().upper()


class DefaultNote(Note):
    def __init__(self, pitch=PITCHES[0], is_long=False):
        super().__init__(pitch, is_long)


class NoteWithOctave(Note):
    def __init__(self, pitch, octave, is_long=False):
        self.octave = octave
        super().__init__(pitch, is_long)

    def __str__(self):
        return f'{super().__str__()} ({self.octave})'