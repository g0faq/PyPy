import pygame


def draw():
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Мишень')
    color_cell = ['red', 'green', 'blue']
    r = n * w
    r2 = n * w
    for c in range(n - 1, -1, -1):
        pygame.draw.circle(screen, color_cell[c % 3], (r - 1,  r - 1), r2)
        r2 -= w


pygame.init()
try:
    w, n = map(int, input().split())
    size = w * n * 2, w * n * 2
    screen = pygame.display.set_mode(size)
    draw()
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
except Exception:
    print('Неправильный формат ввода')
pygame.quit()