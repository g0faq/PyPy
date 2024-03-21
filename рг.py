from random import randrange

import pygame


class Board:
    def __init__(self, width, height, left=10, top=10, cell_size=60, color=(255, 255, 255)):
        self.field = [[0] * width for _ in range(height)]
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.color = ['blue', 'red']
        self.whose_move = 0
        cor = set()
        for i in range(height):
            for j in range(width):
                cor.add((i, j))
        for i in range(width * height):
            x, y = cor.pop()
            self.field[y][x] = randrange(2)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, x, y):
        if self.in_field(x, y):
            x -= self.left
            i = x // self.cell_size
            y -= self.top
            j = y // self.cell_size
            return i, j
        else:
            return None, None

    def in_field(self, x, y):
        max_x = self.width * self.cell_size + self.left
        max_y = self.height * self.cell_size + self.top
        if max_x < x or x < self.left or max_y < y or y < self.top:
            return False
        else:
            return True

    def on_click(self, pushmouse):
        x, y = self.get_cell(*pushmouse)
        if x is None:
            pass
        else:
            if self.whose_move == self.field[y][x]:
                for col in range(self.width):
                    self.field[y][col] = self.whose_move
                for row in range(self.height):
                    self.field[row][x] = self.whose_move
                self.whose_move = (self.whose_move + 1) % 2

    def render(self, screen):
        color = self.color
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.circle(screen, color[self.field[j][i]],
                                   (i * self.cell_size + self.left + self.cell_size // 2,
                                    j * self.cell_size + self.top + self.cell_size // 2),
                                   self.cell_size // 2 - 4)
                pygame.draw.rect(screen, 'white', (i * self.cell_size + self.left, j * self.cell_size + self.top,
                                                   self.cell_size, self.cell_size), 1)

if __name__ == "__main__":
    n = int(input())
    board = Board(n, n)
    board.set_view(10, 10, 480 // n)
    running = True
    size = (500, 500)
    screen = pygame.display.set_mode(size)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.on_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()