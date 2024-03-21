class BigBell:
    def __init__(self):
        self.a = 'ding'
        self.c = 0

    def sound(self):
        if self.c == 0:
            print('ding')
            self.c = 1
        elif self.a == 'ding':
            print('dong')
            self.a = 'dong'
        else:
            print('ding')
            self.a = 'ding'
