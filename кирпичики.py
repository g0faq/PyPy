import pygame

def draw():
    screen.fill('red')
    pygame.display.set_caption('Кирпичи')
    for y in range(0, 200, 30):
        for x in range(0, 300, 30):
            pygame.draw.rect(screen, 'white', (x, y,
                                               30, 15), 1)
    for y in range(15, 200, 30):
        for x in range(-15, 300, 30):
            pygame.draw.rect(screen, 'white', (x, y,
                                               30, 15), 1)

pygame.init()
try:
    wight, height = 300, 200
    size = wight, height
    screen = pygame.display.set_mode(size)
    draw()
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
except Exception:
    print('Неправильный формат ввода')


pygame.quit()