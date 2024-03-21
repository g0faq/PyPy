class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __lt__(self, y):
        maxx = max([self, y], key=lambda x: (x.name, x.x, x.y))
        if maxx == y and y != self:
            return True
        return False

    def __gt__(self, y):
        maxx = max([self, y], key=lambda x: (x.name, x.x, x.y))
        if maxx == self and self != y:
            return True
        return False

    def __le__(self, y):
        maxx = max([self, y], key=lambda x: (x.name, x.x, x.y))
        if maxx == y or self == y:
            return True
        return False

    def __ge__(self, y):
        maxx = max([self, y], key=lambda x: (x.name, x.x, x.y))
        if maxx == self or self == y:
            return True
        return False

    def __eq__(self, y):
        if self.name == y.name and self.x == y.x and self.y == y.y:
            return True
        return False

    def __ne__(self, y):
        if self.name != y.name or self.x != y.x or self.y != y.y:
            return True
        return False

    def __repr__(self):
        return f"Point('{self.name}', {self.x}, {self.y})"

    def __str__(self):
        return self.name + '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def get_coords(self):
        return self.x, self.y