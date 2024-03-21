import pygame


def draw(x, y, r):
    color = 'yellow'
    pygame.draw.circle(screen, color, (x, y), r)


pygame.init()
size = (600, 800)
srcreen = screen = pygame.display.set_mode(size)
pygame.display.set_caption('Жёлтый круг')
screen.fill('blue')
running = True
click = pygame.time.Clock()
x, y, r = 0, 0, 0
drawing = False
EVENT_RADIUS = pygame.USEREVENT + 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            r = 0
            x, y = event.pos
        if event.type == EVENT_RADIUS:
            r += 1
    if drawing:
        draw(x, y, r)
    pygame.time.set_timer(EVENT_RADIUS, 100)
    pygame.display.flip()
    click.tick(50)
pygame.quit()