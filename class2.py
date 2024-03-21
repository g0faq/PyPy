class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.paragraph = []

    def add_word(self, word):
        if not self.paragraph:
            self.paragraph.append(word)
        elif len(self.paragraph[-1]) + len(word) + 1 <= self.width:
            self.paragraph[-1] += ' ' + word
        else:
            self.paragraph.append(word)

    def end(self):
        print('\n'.join(self.paragraph))
        self.paragraph = []


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.paragraph = []

    def add_word(self, word):
        if not self.paragraph:
            self.paragraph.append(word)
        elif len(self.paragraph[-1]) + len(word) + 1 <= self.width:
            self.paragraph[-1] += ' ' + word
        else:
            self.paragraph.append(word)

    def end(self):
        for i in range(len(self.paragraph)):
            self.paragraph[i] = \
                ' ' * (self.width - len(self.paragraph[i])) \
                + self.paragraph[i]
        print('\n'.join(self.paragraph))
        self.paragraph = []