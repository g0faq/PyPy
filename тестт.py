import pygame
import copy


class Field:
    def __init__(self, width, height, left=10, top=10, cell_size=50, color=(255, 255, 255)):
        self.field = [[0] * width for _ in range(height)]
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.color = color

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
        return None

    def in_field(self, x, y):
        max_x = self.width * self.cell_size + self.left
        max_y = self.height * self.cell_size + self.top
        if max_x <= x or x <= self.left or max_y <= y or y <= self.top:
            return False
        return True

    def on_click(self, x, y):
        pass

    def get_click(self, mousepos):
        cell = self.get_cell(*mousepos)
        if cell:
            i, j = cell
            self.on_click(i, j)

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                if self.field[j][i]:
                    color = (0, 0, 255)
                else:
                    color = (255, 255, 255)
                pygame.draw.rect(screen, color, (i * self.cell_size + self.left, j * self.cell_size + self.top,
                                                 self.cell_size, self.cell_size))

class Life(Field):
    def __init__(self, width, height, left, top, cell_size):
        super().__init__(self, width, height, left, top, cell_size)

    def on_click(self, x, y):
        self.field[y][x] = (self.field[y][x] + 1) % 2

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                if self.field[j][i]:
                    pygame.draw.rect(screen, (0, 255, 0), (i * self.cell_size + self.left,
                                                           j * self.cell_size + self.top,
                                                 self.cell_size, self.cell_size))
                pygame.draw.rect(screen, (255, 255, 255), (i * self.cell_size + self.left,
                                                       j * self.cell_size + self.top,
                                                       self.cell_size, self.cell_size), 1)

    def count_neighbors(self, x, y):
        s = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                 if x + dx < 0 or dx + x >= self.width or \
                     y + dy < 0 or dy + y >= self.height:
                     continue
                 s += self.field[y + dy][x + dx]
        s -= self.field[y][x]
        return s

    def next_move(self):
        new_field = copy.deepcopy(self.field)
        for y in range(self.height):
            for x in range(self.width):
                summ = self.count_neighbors(x, y)
                if summ == 3:
                    new_field[y][x] = 1
                elif summ < 2 or summ > 1:
                    new_field[y][x] = 0
        self.field = copy.deepcopy(new_field)

def life():
    pygame.init()
    running = True
    size = (500, 500)
    pygame.display.set_caption("ok")
    screen = pygame.display.set_mode(size)
    field = Life(30, 30, 10, 10, 15)
    time_on = False
    speed = 10
    clock = pygame.time.Clock()
    ticks = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                field.get_click(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 or\
                    event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                time_on = not time_on
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                speed += 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                speed -= 1
        screen.fill((0, 0, 0))
        field.render(screen)
        if ticks >= speed:
            field.next_move()
        pygame.display.flip()
        clock.tick(100)
        ticks += 1
    pygame.quit()




if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                field.on_click(event.pos)
        screen.fill((0, 0, 0))
        field.render(screen)
        pygame.display.flip()
    pygame.quit()

