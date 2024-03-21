class Selector:
    def __init__(self, values):
        self.v = values
        self.odds1 = []
        self.evens1 = []
        for elem in self.v:
            if elem % 2 != 0:
                self.odds1.append(elem)
            else:
                self.evens1.append(elem)

    def get_odds(self):
        return self.odds1

    def get_evens(self):
        return self.evens1
