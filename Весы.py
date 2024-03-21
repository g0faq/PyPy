class Balance:
    def __init__(self):
        self.sl = [0, 0]

    def add_right(self, k):
        self.sl[0] += k

    def add_left(self, k):
        self.sl[1] += k

    def result(self):
        if self.sl[0] > self.sl[1]:
            return 'R'
        elif self.sl[0] < self.sl[1]:
            return 'L'
        else:
            return '='