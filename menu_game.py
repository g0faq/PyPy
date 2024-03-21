import pygame

def draw():
    screen.fill('black')
    pygame.display.set_caption('Прямоугольник')
    pygame.draw.rect(screen, 'green', (0, 0,
                                       300, 100))
    pygame.draw.rect(screen, 'blue', (450, 250,
                                      300, 100))
    pygame.draw.rect(screen, 'red', (900, 500,
                                     300, 100))

    font = pygame.font.Font(None, 50)
    text = font.render("LEVEL 1", True, (0, 0, 0))
    text_x_1, text_y_1 = 70, 30
    screen.blit(text, (text_x_1, text_y_1))

    font = pygame.font.Font(None, 50)
    text = font.render("LEVEL 2", True, (0, 0, 0))
    text_x_2, text_y_2 = wight // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2
    screen.blit(text, (text_x_2, text_y_2))

    font = pygame.font.Font(None, 50)
    text = font.render("LEVEL 3", True, (0, 0, 0))
    text_x_3, text_y_3 = 980, 540
    screen.blit(text, (text_x_3, text_y_3))


pygame.init()
try:
    wight, height = 1200, 600
    size = wight, height
    screen = pygame.display.set_mode(size)
    draw()
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
except Exception:
    print('Неправильный формат ввода')


pygame.quit()