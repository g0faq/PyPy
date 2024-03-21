import pygame
import random


# вычисление цвета
background_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
text_colors = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
pause_color = (0, 0, 255)

# вычисление разрешения экрана
infoObject = pygame.display.Info()
wight_screen = infoObject.current_w
height_screen = infoObject.current_h
size_screen = (wight_screen, height_screen)

# размеры поля
wight_field = 1400
height_field = 700

# вычисление верхней правой точки поля
x_1 = int((wight_screen - wight_field - 100) // 2)
y_1 = int((height_screen - height_field - 100) // 2)
xy_1 = (x_1, y_1)

# вычисление нижней левой точки поля
x_2 = int(x_1 + wight_field)
y_2 = int(y_1 + height_field)
xy_2 = (x_2, y_2)

# вычисление нижней правой поля
x_3 = x_1
y_3 = y_2
xy_3 = (x_3, y_3)

# вычисление верхней левой точки поля
x_4 = x_2
y_4 = y_1
xy_4 = (x_4, y_4)

pause_flag = True

x = x_1
y = random.randint(y_1, y_3)
xy_line = (x, y)
f = 1
color = (255, 255, 255)

mouse_in_break = (215, 0, 0)
mouse_in_pause = (0, 0, 215)

screen = pygame.display.set_mode(size_screen)
screen_1 = pygame.display.set_mode(size_screen)
screen_2 = pygame.display.set_mode(size_screen)
screen_1.fill(background_color)
pygame.draw.polygon(screen_1, (0, 0, 0), ((x_1, y_1), (x_3, y_3), (x_2, y_2), (x_4, y_4)))

running_2 = True

while running_2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_2 = False
        # координаты мыши
        x_mouse = pygame.mouse.get_pos()[0]
        y_mouse = pygame.mouse.get_pos()[1]

        # смена цвета паузы при наведение мыши
        if (x_mouse > wight_screen - 100) and (y_mouse > 100) and (y_mouse < 200):
            if pause_flag:
                mouse_in_pause = (0, 0, 255)
            else:
                mouse_in_pause = (255, 0, 0)
        else:
            if pause_flag:
                mouse_in_pause = (0, 0, 215)
            else:
                mouse_in_pause = (215, 0, 0)
        # смена цвета крестика при наведение мыши
        if (x_mouse > wight_screen - 100) and (y_mouse < 100):
            mouse_in_break = (255, 0, 0)
        else:
            mouse_in_break = (215, 0, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            # пауза
            if (x_mouse > wight_screen - 100) and (y_mouse > 100) and (y_mouse < 200):
                if pause_flag:
                    pause_flag = False
                    pause_color = (0, 0, 255)
                else:
                    pause_flag = True
                    pause_color = (255, 0, 0)

            # цвет линии
            if (x_mouse > wight_screen - 100) and (y_mouse > height_screen - 100):
                color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))

            # крест
            if (x_mouse > wight_screen - 100) and (y_mouse < 100):
                running_2 = False

            # очистка
            if (x_mouse < wight_screen - 100) and (x_mouse > wight_screen - 200) and \
                    (y_mouse > height_screen - 100):
                pygame.draw.polygon(screen, (0, 0, 0), ((x_1, y_1), (x_3, y_3), (x_2, y_2), (x_4, y_4)))
    screen_1 = screen_2

    if pause_flag:
        if ((x == x_1 and y == y_1) or (x == x_2 and y == y_2) or
                (x == x_1 and y == y_2) or (x == x_2 and y == y_1)):
            if f == 1:
                f = 3
            elif f == 2:
                f = 4
            elif f == 3:
                f = 1
            elif f == 4:
                f = 2
        if x < x_1 or x > x_2 or y < y_1 or y > y_2:
            x = x_1
            y = random.randint(y_1, y_2)
        if x == x_2:
            if f == 2:
                x -= 1
                y -= 1
                f = 1
            elif f == 3:
                x -= 1
                y += 1
                f = 4
            xy_line = (x, y)
        elif x == x_1:
            if f == 4:
                x += 1
                y += 1
                f = 3
            elif f == 1:
                x += 1
                y -= 1
                f = 2
            xy_line = (x, y)
        elif y == y_2:
            if f == 3:
                x += 1
                y -= 1
                f = 2
            elif f == 4:
                x -= 1
                y += 1
                f = 1
            xy_line = (x, y)
        elif y == y_1:
            if f == 1:
                x -= 1
                y += 1
                f = 4
            elif f == 2:
                x += 1
                y += 1
                f = 3
            xy_line = (x, y)

        if f == 1:
            x -= 1
            y -= 1
        elif f == 2:
            x += 1
            y -= 1
        elif f == 3:
            x += 1
            y += 1
        elif f == 4:
            x -= 1
            y += 1
        pygame.draw.line(screen, color, xy_line, (x, y), 1)

    # границы поля
    pygame.draw.rect(screen_1, (255, 255, 255), ((x_1 - 10, y_1 - 10), ((x_2 - x_1 + 20), (y_2 - y_1 + 20))), 10)

    # создание кнопок
    # крест
    pygame.draw.line(screen, mouse_in_break, (wight_screen - 80, 20), (wight_screen - 20, 80), 10)
    pygame.draw.line(screen, mouse_in_break, (wight_screen - 20, 20), (wight_screen - 80, 80), 10)

    # пауза
    if not pause_flag:
        pygame.draw.line(screen_1, mouse_in_pause, (wight_screen - 70, 120), (wight_screen - 70, 180), 20)
        pygame.draw.line(screen_1, mouse_in_pause, (wight_screen - 30, 120), (wight_screen - 30, 180), 20)
    else:
        pygame.draw.line(screen_1, mouse_in_pause, (wight_screen - 70, 120), (wight_screen - 70, 180), 20)
        pygame.draw.line(screen_1, mouse_in_pause, (wight_screen - 30, 120), (wight_screen - 30, 180), 20)

    # счётчик
    pygame.draw.rect(screen_1, (0, 0, 0), ((wight_screen // 2 - 125, height_screen - 100),
                                           ((wight_screen // 2 + 125), height_screen)))

    # смена цвета
    pygame.draw.rect(screen_1, color, ((wight_screen - 100, height_screen - 100), (100, 100)))
    pygame.draw.rect(screen_1, (0, 0, 0), ((wight_screen - 100, height_screen - 100), (100, 100)), 1)
    text = pygame.font.Font(None, 36)
    text_line = text.render('LINE', True, text_colors)
    text_color = text.render('COLOR', True, text_colors)
    screen.blit(text_line, (wight_screen - 80, height_screen - 75))
    screen.blit(text_color, (wight_screen - 92, height_screen - 40))
    # очистка
    pygame.draw.rect(screen_1, (0, 0, 0), ((wight_screen - 210, height_screen - 100), (100, 100)), 1)
    text_clear = text.render('CLEAR', True, text_colors)
    screen_1.blit(text_clear, (wight_screen - 202, height_screen - 57))
    clock = pygame.time.Clock()

    pygame.display.flip()
    clock.tick(12500)
pygame.quit()