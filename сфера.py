import pygame


def draw():
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Сфера')
    y = 0
    height = 300
    wight = 150 // n
    for i in range(n):
        x = 150 - (i + 1) * wight
        pygame.draw.ellipse(screen, 'white', (x, y, wight * 2 * (i + 1), height), 1)
    x = 0
    wight = 300
    height = 150 // n
    for i in range(n):
        y = 150 - (i + 1) * height
        pygame.draw.ellipse(screen, 'white', (x, y, wight, height * 2 * (i + 1)), 1)

pygame.init()
try:
    n = int(input())
    size = 300, 300
    screen = pygame.display.set_mode(size)
    draw()
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass 
except Exception:
    print('Неправильный формат ввода')
pygame.quit()