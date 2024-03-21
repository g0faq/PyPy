import pygame
from random import choice

COLORS = ['white', 'red', 'blue', 'green', 'yellow', 'pink']
pygame.init()
size = w, h = 1800, 1000
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Шарики')
bolls = []
EVENT_BOLL = pygame.USEREVENT + 1
pygame.time.set_timer(EVENT_BOLL, 10)
drawing = False
running = True
click = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            x, y = event.pos
            c = choice(COLORS)
            bolls.append([x, y, -1, -1, c])
        if event.type == EVENT_BOLL:
            for element in bolls:
                if element[1] <= 10 or element[1] >= h - 10:
                    element[3] = -element[3]
                if element[0] <= 10 or element[0] >= w - 10:
                    element[2] = -element[2]
                element[0] += element[2]
                element[1] += element[3]
    screen.fill('black')
    if drawing:
        for element in bolls:
            pygame.draw.circle(screen, element[4], (element[0], element[1]), 10)

    click.tick(50)
    pygame.display.flip()
pygame.quit()