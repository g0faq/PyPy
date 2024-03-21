import pygame


def draw(count):
    screen.fill('black')
    pygame.display.set_caption('...')

    font = pygame.font.Font(None, 100)
    text = font.render(str(count), True, 'red')
    text_x, text_y = wight // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


pygame.init()

count = 1
wight, height = 200, 200
size = wight, height
screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.WINDOWEVENT:
            if event.event == pygame.WINDOWEVENT_MINIMIZED:
                count += 1
    draw(count)
    pygame.display.flip()

pygame.quit()