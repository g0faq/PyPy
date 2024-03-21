import pygame


def draw():
    screen.fill('yellow')
    pygame.display.set_caption('Ромбики')
    for i in range(0, width, n):
        for j in range(0, height, n):
            if j + n > height or i + n > width:
                continue
            pygame.draw.polygon(screen, 'orange', [(i + n / 2, j),
                                                   (i + n, j + n / 2),
                                                   (i + n / 2, j + n),
                                                   (i, j + n / 2)])


pygame.init()
try:
    n = int(input())
    size = width, height = (300, 300)
    screen = pygame.display.set_mode(size)
    draw()
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
except Exception:
    print('Неправильный формат ввода')
pygame.quit()