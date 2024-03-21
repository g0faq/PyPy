import pygame


def draw():
    screen.fill((0, 0, 0))
    d = a // n
    if n % 2:
        color_cell = 'black'
    else:
        color_cell = 'white'
    for y in range(0, a, d):
        for x in range(0, a, d):
            pygame.draw.rect(screen, color_cell, (x, y, x + d, y + d))
            if color_cell == 'black':
                color_cell = 'white'
            else:
                color_cell = 'black'

        if n % 2 == 0:
            if color_cell == 'black':
                color_cell = 'white'
            else:
                color_cell = 'black'


pygame.init()
try:
    a, n = map(int, input().split())
    size = a, a
    screen = pygame.display.set_mode(size)
    draw()
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
except Exception:
    print('Неправильный формат ввода')
