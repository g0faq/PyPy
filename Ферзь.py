def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Queen:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_color(self):
        return self.color

    def char(self):
        return 'Q'

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        elif self.row == row or self.col == col or \
                self.row + self.col == row + col or \
                self.row - self.col == row - col:
            return True
        else:
            return False
