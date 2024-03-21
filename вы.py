class BoundingRectangle:
    def __init__(self):
        self.min_y = 0
        self.max_y = 0
        self.min_x = 0
        self.max_x = 0
        self.p1 = True

    def add_point(self, x, y):
        if self.p1:
            self.min_y = y
            self.max_y = y
            self.min_x = x
            self.max_x = x
            self.p1 = False
        else:
            self.min_y = min(y, self.min_y)
            self.max_y = max(y, self.max_y)
            self.min_x = min(x, self.min_x)
            self.max_x = max(x, self.max_x)

    def width(self):
        return self.max_x - self.min_x

    def height(self):
        return self.max_y - self.min_y

    def bottom_y(self):
        return self.min_y

    def top_y(self):
        return self.max_y

    def left_x(self):
        return self.min_x

    def right_x(self):
        return self.max_x
