class MinMaxWordFinder:
    def __init__(self):
        self._max = 0
        self._min = 10000000
        self.short = []
        self.long = []

    def add_sentence(self, s):
        for elem in s.split():
            if self._max == len(elem):
                self.long.append(elem)
            elif self._max < len(elem):
                self.long = []
                self.long.append(elem)
                self._max = len(elem)
            if self._min == len(elem):
                self.short.append(elem)
            elif self._min > len(elem):
                self.short = []
                self.short.append(elem)
                self._min = len(elem)

    def shortest_words(self):
        return sorted(self.short)

    def longest_words(self):
        return sorted(list(set(self.long)))