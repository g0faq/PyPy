import pygame


def draw():
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Прямоугольник')
    pygame.draw.rect(screen, 'RED', (1, 1,
                                     wight - 1, height - 1))


pygame.init()
try:
    wight, height = map(int, input().split())
    size = wight, height
    screen = pygame.display.set_mode(size)
    draw()
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
except Exception:
    print('Неправильный формат ввода')


pygame.quit()