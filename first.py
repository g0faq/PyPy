import pygame


def draw():
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Крест')
    pygame.draw.line(screen, (255, 255, 255), [0, 0], [wight, height], 5)
    pygame.draw.line(screen, (255, 255, 255), [0, height], [wight, 0], 5)


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



