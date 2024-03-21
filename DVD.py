import pygame
import random

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1100, 800

    x = 0
    y = 300
    xy_line = (0, 0)
    f = 1
    flag = True
    mouse_color_flag_pause = True
    colors = ['yellow', 'red', 'blue', 'white', 'green', 'purple']
    color = colors[random.randint(0, len(colors) - 1)]
    count = 0
    v = 1

    screen = pygame.display.set_mode(size)
    screen_2 = pygame.display.set_mode(size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse = pygame.mouse.get_pos()[0]
                y_mouse = pygame.mouse.get_pos()[1]
                if x_mouse > width - 100 and y_mouse < height // 4:
                    if flag:
                        flag = False
                        mouse_color_flag_pause = False
                    else:
                        flag = True
                        mouse_color_flag_pause = True

                if (x_mouse > width - 100) and (y_mouse > height // 4) and (y_mouse < height // 2):
                    color = colors[random.randint(0, len(colors) - 1)]

                if (x_mouse > width - 100) and (y_mouse > height // 4 * 3):
                    running = False

                if (x_mouse > width - 100) and (y_mouse > height // 2) and (y_mouse < height // 4 * 3):
                    screen = pygame.display.set_mode(size)
                    screen_2 = pygame.display.set_mode(size)
        screen = screen_2
        if flag:
            if x == width - 100:
                if f == 2:
                    x -= v
                    y -= v
                    f = 1
                elif f == 3:
                    x -= v
                    y += v
                    f = 4
                xy_line = (x, y)
            elif x == 0:
                if f == 4:
                    x += v
                    y += v
                    f = 3
                elif f == 1:
                    x += v
                    y -= v
                    f = 2
                xy_line = (x, y)
            elif y == height:
                if f == 3:
                    x += v
                    y -= v
                    f = 2
                elif f == 4:
                    x -= v
                    y += v
                    f = 1
                xy_line = (x, y)
            elif y == 0:
                if f == 1:
                    x -= v
                    y += v
                    f = 4
                elif f == 2:
                    x += v
                    y += v
                    f = 3
                xy_line = (x, y)

            if f == 1:
                x -= v
                y -= v
            elif f == 2:
                x += v
                y -= v
            elif f == 3:
                x += v
                y += v
            elif f == 4:
                x -= v
                y += v

            pygame.draw.line(screen, color, xy_line, (x, y), 1)
            count += 1

        pygame.draw.line(screen, (255, 0, 0), (width - 95, 0), (width - 95, height), 10)

        pygame.draw.line(screen, (255, 0, 0), (width - 95, height // 4), (width, height // 4), 10)
        pygame.draw.line(screen, (255, 0, 0), (width - 95, height // 2), (width, height // 2), 10)
        pygame.draw.line(screen, (255, 0, 0), (width - 95, height // 4 * 3), (width, height // 4 * 3), 10)

        if mouse_color_flag_pause:
            pygame.draw.line(screen, (0, 0, 255), (1042, 75), (1042, 125), 10)
            pygame.draw.line(screen, (0, 0, 255), (1065, 75), (1065, 125), 10)
        else:
            pygame.draw.line(screen, (255, 0, 0), (1042, 75), (1042, 125), 10)
            pygame.draw.line(screen, (255, 0, 0), (1065, 75), (1065, 125), 10)

        te = pygame.font.Font(None, 36)
        text = te.render('COLOR', True, (180, 0, 0))
        screen.blit(text, (1010, 300))

        pygame.draw.line(screen, (255, 0, 0), (1042, 675), (1065, 725), 10)
        pygame.draw.line(screen, (255, 0, 0), (1065, 675), (1042, 725), 10)

        te = pygame.font.Font(None, 36)
        text = te.render('CLEAR', True, (180, 0, 0))
        screen.blit(text, (1010, 500))

        pygame.display.flip()
    pygame.quit()