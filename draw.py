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
wight_field = random.randint(50, wight_screen)
height_field = random.randint(50, height_screen)

# вычисление верхней правой точки поля
x_1 = int((wight_screen - wight_field - 100) // 2)
y_1 = int((height_screen - height_field) // 2)
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

# флаг паузы
pause_flag = True

# вычисление начальных координат линии
x = random.randint(x_1, x_4)
y = random.randint(y_1, y_3)
xy_line = (x, y)

# направление линии
f = 1

# начальный цвет линии
color = (255, 255, 255)

if __name__ == '__main__':
    pygame.init()

    # создание экарана
    screen = pygame.display.set_mode(size_screen)
    screen_2 = pygame.display.set_mode(size_screen)
    screen.fill(background_color)

    # создание поля
    pygame.draw.polygon(screen, (0, 0, 0), ((x_1, y_1), (x_3, y_3), (x_2, y_2), (x_4, y_4)))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse = pygame.mouse.get_pos()[0]
                y_mouse = pygame.mouse.get_pos()[1]
                if x_mouse > wight_screen - 100 and y_mouse < 100:
                    if pause_flag:
                        pause_flag = False
                        pause_color = (255, 0, 0)
                    else:
                        pause_flag = True
                        pause_color = (0, 0, 255)

                if (x_mouse > wight_screen - 100) and (y_mouse > 100) and (y_mouse < 200):
                    color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))

                if (x_mouse > wight_screen - 100) and (y_mouse > 300):
                    running = False

                if (x_mouse > wight_screen - 100) and (y_mouse > 200) and (y_mouse < 300):
                    pygame.draw.polygon(screen, (0, 0, 0), ((x_1, y_1), (x_3, y_3), (x_2, y_2), (x_4, y_4)))
        screen = screen_2

        if pause_flag:
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
        pygame.draw.line(screen, (255, 255, 255), (x_1 - 5, y_1 - 5), (x_4 + 5, y_4 - 5), 10)
        pygame.draw.line(screen, (255, 255, 255), (x_1 - 5, y_1 - 5), (x_3 - 5, y_3 + 5), 10)
        pygame.draw.line(screen, (255, 255, 255), (x_3 - 5, y_3 + 5), (x_2 + 5, y_2 + 5), 10)
        pygame.draw.line(screen, (255, 255, 255), (x_2 + 5, y_2 + 5), (x_4 + 5, y_4 - 5), 10)

        # заготовка для кнопок
        pygame.draw.polygon(screen, (0, 0, 0), ((wight_screen - 100, 0), (wight_screen - 100, 400),
                                                (wight_screen, 400), (wight_screen, 0)))
        # постоение контура кнопок
        pygame.draw.line(screen, (255, 0, 0), (wight_screen - 100, height_screen - 5),
                         (wight_screen, height_screen - 5), 10)
        pygame.draw.line(screen, background_color, (wight_screen - 100, 0), (wight_screen, 0), 10)
        pygame.draw.line(screen, background_color, (wight_screen - 100, 0), (wight_screen - 100, 400), 10)
        pygame.draw.line(screen, background_color, (wight_screen - 100, 100), (wight_screen, 100), 10)
        pygame.draw.line(screen, background_color, (wight_screen - 100, 200), (wight_screen, 200), 10)
        pygame.draw.line(screen, background_color, (wight_screen - 100, 300), (wight_screen, 300), 10)
        pygame.draw.line(screen, background_color, (wight_screen - 104, 400), (wight_screen, 400), 10)

        # создание кнопок
        # крест
        pygame.draw.line(screen, (255, 0, 0), (wight_screen - 80, 320), (wight_screen - 20, 380), 10)
        pygame.draw.line(screen, (255, 0, 0), (wight_screen - 20, 320), (wight_screen - 80, 380), 10)
        # пауза
        if not pause_flag:
            pygame.draw.line(screen, (255, 0, 0), (wight_screen - 70, 20), (wight_screen - 70, 80), 20)
            pygame.draw.line(screen, (255, 0, 0), (wight_screen - 30, 20), (wight_screen - 30, 80), 20)
        else:
            pygame.draw.line(screen, (0, 0, 255), (wight_screen - 70, 20), (wight_screen - 70, 80), 20)
            pygame.draw.line(screen, (0, 0, 255), (wight_screen - 30, 20), (wight_screen - 30, 80), 20)
        # смена цвета
        text = pygame.font.Font(None, 36)

        text_color = text.render('COLOR', True, text_colors)
        screen.blit(text_color, (wight_screen - 90, 140))
        # очистка
        text_clear = text.render('CLEAR', True, text_colors)
        screen.blit(text_clear, (wight_screen - 90, 240))

        pygame.display.flip()
pygame.quit()