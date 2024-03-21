class LittleBell:
    def sound(self):
        print('ding')


class BigBell:
    count = 0
    
    def sound(self):
        if self.count % 2 == 0:
            print('ding')
        else:
            print('dong')
        self.count += 1


class BellTower:
    def __init__(self, *args):
        self.bells = []
        for elem in args:
            self.bells.append(elem)

    def append(self, bell):
        self.bells.append(bell)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print('...')