class OddEvenSeparator:
    def __init__(self):
        self.psp = []
        self.sp1 = []
        self.sp2 = []

    def add_number(self, num):
        self.psp.append(num)
        if num % 2 == 0:
            self.sp1.append(num)
        else:
            self.sp2.append(num)

    def even(self):
        return self.sp1

    def odd(self):
        return self.sp2
