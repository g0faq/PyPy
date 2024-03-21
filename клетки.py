import pygame


class Board:
    def __init__(self, width, height, left=100, top=40, cell_size=60, color=(255, 255, 255)):
        self.field = [[-1] * width for _ in range(height)]
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.color = color
        self.count = 0

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
            print(None)
        else:
            if self.field[y][x] == -1:
                self.count += 1
                self.field[y][x] = self.count % 2

    def render(self, screen):
        color = [pygame.Color('black'), pygame.Color('red'), pygame.Color('blue')]
        for i in range(self.width):
            for j in range(self.height):
                if self.field[j][i] == 1:
                    pygame.draw.line(screen, 'blue',
                                     (i * self.cell_size + self.left + 4, j * self.cell_size + self.top + 4),
                                     (i * self.cell_size + self.left + self.cell_size - 4,
                                      j * self.cell_size + self.top + self.cell_size - 4),
                                     2)
                    pygame.draw.line(screen, 'blue',
                                     (i * self.cell_size + self.left + 4,
                                      j * self.cell_size + self.top + self.cell_size - 4),
                                     (i * self.cell_size + self.left + self.cell_size - 4,
                                      j * self.cell_size + self.top + 4),
                                      2)
                elif self.field[j][i] == 0:
                    pygame.draw.circle(screen, 'red',
                                       (i * self.cell_size + self.left + self.cell_size // 2,
                                        j * self.cell_size + self.top + self.cell_size // 2),
                                       self.cell_size // 2 - 4,
                                       2)
                pygame.draw.rect(screen, 'white', (i * self.cell_size + self.left, j * self.cell_size + self.top,
                                                   self.cell_size, self.cell_size), 1)

if __name__ == "__main__":
    board = Board(5, 7)
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