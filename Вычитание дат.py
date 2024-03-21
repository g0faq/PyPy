class Date:
    def __init__(self, month, day):
        self.x = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.y = sum(self.x[:month]) + day

    def __sub__(self, other):
        return self.y - other.y