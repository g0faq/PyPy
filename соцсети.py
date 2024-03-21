class User:
    def __init__(self, n):
        self.n = n

    def send_message(self, u, m):
        pass

    def post(self, m):
        pass

    def info(self):
        return ''

    def describe(self):
        print(self.n, self.info(), sep='\n')


class Person(User):
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def info(self):
        return 'Дата рождения: ' + self.d

    def subscribe(self, u):
        pass


class Community(User):
    def __init__(self, n, o):
        self.n = n
        self.o = o

    def info(self):
        return 'Описание: ' + self.o