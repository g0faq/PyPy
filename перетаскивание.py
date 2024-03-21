import pygame


pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Перетаскивание')
screen.fill('black')
x, y = 0, 0
a = 100
screen.fill('green', pygame.Rect(x, y, a, a))
running = True
dragging = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x <= event.pos[0] < x + a and y <= event.pos[1] < y + a:
                dragging = True
        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        if dragging and event.type == pygame.MOUSEMOTION:
            x, y = x + event.rel[0], y + event.rel[1]
            screen.fill('black')
            screen.fill('green', pygame.Rect(x, y, a, a))
    pygame.display.flip()
pygame.quit()