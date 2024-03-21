import pygame

x1, y1, h1, w1, x2, y2, h2, w2 = map(int, '100 100 200 200 200 200 200 200'.split())
xh1 = x1 + h1
yw1 = y1 + w1
xh2 = x2 + h2
yw2 = y2 + w2
x1, y1 = y1, x1
xh1, yw1 = yw1, xh1
x2, y2 = y2, x2
xh2, yw2 = yw2, xh2
color = (175, 0, 175)

if __name__ == '__main__':
    pygame.init()

    infoObject = pygame.display.Info()
    wight_screen = infoObject.current_w
    height_screen = infoObject.current_h
    size_screen = (wight_screen, height_screen)
    screen = pygame.display.set_mode(size_screen)
    screen.fill((0, 0, 0))

    pygame.draw.polygon(screen, (255, 0, 0), ((x1, y1), (xh1, y1), (xh1, yw1), (x1, yw1)), 2)
    pygame.draw.polygon(screen, (0, 0, 255), ((x2, y2), (xh2, y2), (xh2, yw2), (x2, yw2)), 2)
    x1 += 2
    x2 += 2
    y1 += 2
    y2 += 2
    xh1 -= 2
    xh2 -= 2
    yw1 -= 2
    yw2 -= 2

    mouse_in_break = (255, 0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            x_mouse = pygame.mouse.get_pos()[0]
            y_mouse = pygame.mouse.get_pos()[1]

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (x_mouse > wight_screen - 100) and (y_mouse < 100):
                    running = False
            if (x_mouse > wight_screen - 100) and (y_mouse < 100):
                mouse_in_break = (255, 0, 0)
            else:
                mouse_in_break = (215, 0, 0)

        pygame.draw.line(screen, mouse_in_break, (wight_screen - 80, 20), (wight_screen - 20, 80), 10)
        pygame.draw.line(screen, mouse_in_break, (wight_screen - 20, 20), (wight_screen - 80, 80), 10)

        if x1 < x2 < xh2 < xh1:
            if y2 < y1 < yw2 < yw1:
                pygame.draw.polygon(screen, color, ((x2, x1), (xh2, y1), (xh2, yw2), (x2, yw2)))
            if y1 < y2 < yw1 < yw2:
                pygame.draw.polygon(screen, color, ((x2, y2), (xh2, y2), (xh2, yw1), (x2, yw1)))

        if y1 < y2 < yw2 < yw1:
            if x2 < x1 < xh2 < xh1:
                pygame.draw.polygon(screen, color, ((x1, y2), (xh2, y2), (xh2, yw2), (x1, yw2)))
            if x1 < x2 < xh1 < xh2:
                pygame.draw.polygon(screen, color, ((x2, y2), (xh1, y2), (xh1, yw2), (x2, yw2)))

        if (x2 < x1 < xh2 < xh1) and (y1 < y2 < yw1 < yw2):
            pygame.draw.polygon(screen, color, ((x1, y2), (xh2, y2), (xh2, yw1), (x1, yw1)))
        if (x2 < x1 < xh2 < xh1) and (y2 < y1 < yw2 < yw1):
            pygame.draw.polygon(screen, color, ((x1, y1), (xh2, y1), (xh2, yw2), (x1, yw2)))
        if (x1 < x2 < xh1 < xh2) and (y2 < y1 < yw2 < yw1):
            pygame.draw.polygon(screen, color, ((x2, yw1), (xh1, y1), (xh1, yw2), (x2, yw2)))
        if (x1 < x2 < xh1 < xh2) and (y1 < y2 < yw1 < yw2):
            pygame.draw.polygon(screen, color, ((x2, y2), (xh1, y2), (xh1, yw1), (x2, yw1)))

        if (x1 < x2 < xh2 < xh1) and (y1 < y2 < yw2 < yw1):
            pygame.draw.polygon(screen, color, ((x2, y2), (xh2, y2), (xh2, yw2), (x2, yw2)))
        if (x2 < x1 < xh1 < xh2) and (y2 < y1 < yw1 < yw2):
            pygame.draw.polygon(screen, color, ((x1, y1), (xh1, y1), (xh1, yw1), (x1, yw1)))

        if x2 < x1 < xh1 < xh2:
            if y2 < y1 < yw2 < yw1:
                pygame.draw.polygon(screen, color, ((x1, y1), (xh1, y1), (xh1, yw2), (x1, yw2)))
            if y1 < y2 < yw1 < yw2:
                pygame.draw.polygon(screen, color, ((x1, y2), (xh1, y2), (xh1, yw1), (x1, yw1)))
        if y2 < y1 < yw1 < yw2:
            if x2 < x1 < xh2 < xh1:
                pygame.draw.polygon(screen, color, ((x1, y1), (xh2, y1), (xh2, yw1), (x1, yw1)))
            if x1 < x2 < xh1 < xh2:
                pygame.draw.polygon(screen, color, ((x2, y1), (xh1, y1), (xh1, yw1), (x2, yw1)))

        if (x2 < x1 < xh1 < xh2) and (y1 < y2 < yw2 < yw1):
            pygame.draw.polygon(screen, color, ((x1, y2), (xh1, y2), (xh1, yw2), (x1, yw2)))
        if (x1 < x2 < xh2 < xh1) and (y2 < y1 < yw1 < yw2):
            pygame.draw.polygon(screen, color, ((x2, y1), (xh2, y1), (xh2, yw1), (x2, yw1)))

        pygame.display.flip()
    pygame.quit()