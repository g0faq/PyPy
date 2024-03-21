def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Knight:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'N'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        elif (self.row - 2 == row or self.row + 2 == row) and \
                (self.col - 1 == col or self.col + 1 == col):
            return True
        elif (self.row - 1 == row or self.row + 1 == row) and \
                (self.col - 2 == col or self.col + 2 == col):
            return True
        return False