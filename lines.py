import random
import pygame


if __name__ == '__main__':
    pygame.init()

    running_2 = False
    # нахождение цветов
    background_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
    color_text = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
    color_button = (0, 0, 0)

    # вычисление разрешения экаран
    infoObject = pygame.display.Info()
    wight_screen = infoObject.current_w
    height_screen = infoObject.current_h
    size_screen = (wight_screen, height_screen)

    screen = pygame.display.set_mode(size_screen)
    running = True

    # заливка экрана
    screen.fill(background_color)

    fps = 0

    wight = 200
    height = 100

    mouse_in_break = (255, 0, 0)

    # цвета кнопок минус и плюс
    color_wight_minus = (255, 0, 0)
    color_height_minus = (255, 0, 0)
    color_wight_plus = (0, 0, 255)
    color_height_plus = (0, 0, 255)
    color_speed_minus = (255, 0, 0)
    color_speed_plus = (0, 0, 255)

    color_start = (0, 255, 0)

    color = (255, 255, 255)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            x_mouse = pygame.mouse.get_pos()[0]
            y_mouse = pygame.mouse.get_pos()[1]
            if (x_mouse > wight_screen - 290) and (y_mouse > height_screen - 150):
                color_start = (0, 255, 0)
            else:
                color_start = (0, 215, 0)
            if (x_mouse > wight_screen - 100) and (y_mouse < 100):
                mouse_in_break = (255, 0, 0)
            else:
                mouse_in_break = (215, 0, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # смена цвета линии
                if (x_mouse > 200) and (y_mouse > height_screen - 100) and (x_mouse < 300):
                    color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                # ширина -
                if (x_mouse > 450) and (x_mouse < 550) and (y_mouse > 125) and (y_mouse < 225):
                    if wight > 200:
                        wight -= 100
                        color_wight_minus = (0, 0, 255)
                        color_wight_plus = (0, 0, 255)
                    else:
                        color_wight_minus = (255, 0, 0)
                # высота -
                if (x_mouse > 450) and (x_mouse < 550) and (y_mouse > 325) and (y_mouse < 425):
                    if height > 100:
                        height -= 100
                        color_height_minus = (0, 0, 255)
                        color_height_plus = (0, 0, 255)
                    else:
                        color_height_minus = (255, 0, 0)
                # скорость -
                if (x_mouse > 450) and (x_mouse < 550) and (y_mouse > 525) and (y_mouse < 625):
                    if fps > 250:
                        fps -= 250
                        color_speed_minus = (0, 0, 255)
                # ширина +
                if (x_mouse > 950) and (x_mouse < 1050) and (y_mouse > 125) and (y_mouse < 225):
                    if wight + 100 < wight_screen - 110:
                        wight += 100
                        color_wight_plus = (0, 0, 255)
                        color_wight_minus = (0, 0, 255)
                    else:
                        color_wight_plus = (255, 0, 0)
                # высота +
                if (x_mouse > 950) and (x_mouse < 1050) and (y_mouse > 325) and (y_mouse < 425):
                    if height + 100 < height_screen - 150:
                        height += 100
                        color_height_plus = (0, 0, 255)
                        color_height_minus = (0, 0, 255)
                    else:
                        color_height_plus = (255, 0, 0)
                # скорость +
                if (x_mouse > 950) and (x_mouse < 1050) and (y_mouse > 525) and (y_mouse < 625):
                    fps += 250
                    color_speed_minus = (0, 0, 255)
                # кнопка старт
                if (x_mouse > wight_screen - 300) and (y_mouse > height_screen - 110):
                    running_2 = True
                    running = False
                # закрытие программы
                if (x_mouse > wight_screen - 100) and (y_mouse < 100):
                    running = False
                # смена цвета фона
                if (x_mouse < 100) and (y_mouse > height_screen - 100):
                    background_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                    screen.fill(background_color)
                # смена цвета текста
                if (x_mouse < 200) and (x_mouse > 100) and (y_mouse > height_screen - 100):
                    color_text = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                # рандом
                if ((x_mouse > 1150) and (x_mouse < 1450) and
                    (y_mouse > 200) and (y_mouse < 350)):
                    list_wight = []
                    list_height = []
                    for w in range(200, wight_screen - 110, 100):
                        list_wight.append(w)
                    for h in range(100, height_screen - 110, 100):
                        list_height.append(h)
                    wight = list_wight[random.randint(0, len(list_wight) - 1)]
                    height = list_height[random.randint(0, len(list_height) - 1)]
                    if wight == 200:
                        color_wight_minus = (255, 0, 0)
                    else:
                        color_wight_minus = (0, 0, 255)
                    if wight + 100 >= wight_screen - 110:
                        color_wight_plus = (255, 0, 0)
                    else:
                        color_wight_plus = (0, 0, 255)
                    if height == 100:
                        color_height_minus = (255, 0, 0)
                    else:
                        color_height_minus = (0, 0, 255)
                    if height + 100 >= height_screen - 110:
                        color_height_plus = (255, 0, 0)
                    else:
                        color_height_plus = (0, 0, 255)
            # смена цвета кнопок
            if wight == 200:
                color_wight_minus = (255, 0, 0)
            if wight + 100 >= wight_screen - 110:
                color_wight_plus = (255, 0, 0)
            if height == 100:
                color_height_minus = (255, 0, 0)
            if height + 100 >= height_screen - 110:
                color_height_plus = (255, 0, 0)
            if fps == 50:
                color_speed_minus = (255, 0, 0)

        # кнопка рандом
        text_random = pygame.font.Font(None, 70)
        pygame.draw.rect(screen, color_button, ((1150, 200), (300, 150)))
        text_start = text_random.render('RANDOM', True, color_text)
        screen.blit(text_start, (1185, 250))

        # шаблон для кнопок (ширина/высота)
        pygame.draw.rect(screen, color_button, ((100, 100), (300, 150)))
        pygame.draw.rect(screen, color_button, ((100, 300), (300, 150)))

        # шаблон для кнопок скорости
        pygame.draw.rect(screen, color_button, ((100, 500), (300, 150)))
        pygame.draw.rect(screen, color_button, ((600, 500), (300, 150)))
        pygame.draw.rect(screen, color_button, ((450, 525), (100, 100)))
        pygame.draw.rect(screen, color_button, ((950, 525), (100, 100)))

        # текст
        text = pygame.font.Font(None, 70)
        text_wight = text.render('ШИРИНА', True, color_text)
        text_height = text.render('ВЫСОТА', True, color_text)
        text_speed = text.render('СКОРОСТЬ', True, color_text)
        screen.blit(text_wight, (130, 150))
        screen.blit(text_height, (135, 350))
        screen.blit(text_speed, (117, 550))

        # кнопки для минусов
        pygame.draw.rect(screen, color_button, ((450, 125), (100, 100)))
        pygame.draw.rect(screen, color_button, ((450, 325), (100, 100)))

        # шаблон для выводы ширины/высоты
        pygame.draw.rect(screen, color_button, ((600, 100), (300, 150)))
        pygame.draw.rect(screen, color_button, ((600, 300), (300, 150)))

        # кнопки для плюсов
        pygame.draw.rect(screen, color_button, ((950, 125), (100, 100)))
        pygame.draw.rect(screen, color_button, ((950, 325), (100, 100)))

        # текст
        text_1 = pygame.font.Font(None, 150)
        text_plus_wight = text_1.render('+', True, color_wight_plus)
        text_minus_wight = text_1.render('-', True, color_wight_minus)
        text_plus_height = text_1.render('+', True, color_height_plus)
        text_minus_height = text_1.render('-', True, color_height_minus)
        text_minus_speed = text_1.render('-', True, color_speed_minus)
        text_plus_speed = text_1.render('+', True, color_speed_plus)
        text_count_wight = text.render(str(wight), True, color_text)
        text_count_height = text.render(str(height), True, color_text)
        text_fps = text.render(str(fps // 50), True, color_text)
        screen.blit(text_plus_wight, (970, 115))
        screen.blit(text_plus_height, (970, 315))
        screen.blit(text_plus_speed, (970, 515))
        screen.blit(text_minus_wight, (480, 120))
        screen.blit(text_minus_height, (480, 320))
        screen.blit(text_minus_speed, (480, 520))
        screen.blit(text_count_wight, (690, 150))
        screen.blit(text_count_height, (690, 350))
        screen.blit(text_fps, (725, 550))

        # кнопка старт
        pygame.draw.rect(screen, color_start, ((wight_screen - 290, height_screen - 150), (290, 150)))
        text_start = text.render('START', True, (0, 0, 0))
        screen.blit(text_start, (wight_screen - 230, height_screen - 100))

        # крест
        pygame.draw.line(screen, mouse_in_break, (wight_screen - 80, 20), (wight_screen - 20, 80), 10)
        pygame.draw.line(screen, mouse_in_break, (wight_screen - 20, 20), (wight_screen - 80, 80), 10)

        # кнопки смены цветов
        pygame.draw.rect(screen, (255, 255, 255), ((0, height_screen - 100), (100, 100)), 1)
        pygame.draw.rect(screen, (255, 255, 255), ((100, height_screen - 100), (100, 100)), 1)
        text_color_change = pygame.font.Font(None, 36)
        texts_color = text_color_change.render('COLOR', True, color_text)
        text_color_fond = text_color_change.render('FOND', True, color_text)
        text_color = text_color_change.render('TEXT', True, color_text)
        screen.blit(text_color_fond, (15, height_screen - 75))
        screen.blit(texts_color, (103, height_screen - 40))
        screen.blit(text_color, (115, height_screen - 75))
        screen.blit(texts_color, (3, height_screen - 40))
        pygame.display.flip()

        pygame.draw.rect(screen, color, ((200, height_screen - 100), (100, 100)))
        pygame.draw.rect(screen, (255, 255, 255), ((200, height_screen - 100), (100, 100)), 1)
        text = pygame.font.Font(None, 36)
        text_line = text.render('LINE', True, color_text)
        text_color = text.render('COLOR', True, color_text)
        screen.blit(text_line, (220, height_screen - 75))
        screen.blit(text_color, (208, height_screen - 40))


    pause_color = (0, 0, 255)

    # вычисление разрешения экрана
    infoObject = pygame.display.Info()
    wight_screen = infoObject.current_w
    height_screen = infoObject.current_h
    size_screen = (wight_screen, height_screen)

    # размеры поля
    wight_field = wight
    height_field = height

    # вычисление верхней левой точки поля
    x_1 = int((wight_screen - wight_field - 100) // 2)
    y_1 = int((height_screen - height_field - 100) // 2)
    xy_1 = (x_1, y_1)

    # вычисление нижней правой точки поля
    x_2 = int(x_1 + wight_field)
    y_2 = int(y_1 + height_field)
    xy_2 = (x_2, y_2)

    # вычисление нижней левой поля
    x_3 = x_1
    y_3 = y_2
    xy_3 = (x_3, y_3)

    # вычисление верхней правой точки поля
    x_4 = x_2
    y_4 = y_1
    xy_4 = (x_4, y_4)

    pause_flag = True

    x = random.randint(x_1, x_3)
    y = random.randint(y_1, y_3)
    xy_line = (x, y)
    f = 1
    last_f = 1
    count_wall = 0
    count_corner = 0

    mouse_in_break = (215, 0, 0)
    mouse_in_pause = (0, 0, 215)

    screen_1 = pygame.display.set_mode(size_screen)
    screen_2 = pygame.display.set_mode(size_screen)
    screen_1.fill(background_color)
    pygame.draw.polygon(screen_1, (0, 0, 0), ((x_1, y_1), (x_3, y_3), (x_2, y_2), (x_4, y_4)))

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
                if (x_mouse < wight_screen - 100) and (x_mouse > wight_screen - 200) and\
                        (y_mouse > height_screen - 100):
                    pygame.draw.polygon(screen, (0, 0, 0), ((x_1, y_1), (x_3, y_3), (x_2, y_2), (x_4, y_4)))
                    count_wall = 0
                    count_corner = 0
        screen_1 = screen_2

        if pause_flag:
            if ((x == x_1 and y == y_1) or (x == x_2 and y == y_2) or
                    (x == x_1 and y == y_2) or (x == x_2 and y == y_1)):
                if f == 1:
                    f = 3
                    last_f = 1
                elif f == 2:
                    f = 4
                    last_f = 2
                elif f == 3:
                    f = 1
                    last_f = 3
                elif f == 4:
                    f = 2
                    last_f = 4
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
            pygame.draw.line(screen, color, xy_line, (x, y), 2)

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
        pygame.draw.rect(screen_1, (0, 0, 0), ((wight_screen // 2 - 305, height_screen - 90), (300, 90)))
        pygame.draw.rect(screen_1, (0, 0, 0), ((wight_screen // 2 + 5, height_screen - 90), (300, 90)))

        if (x == x_1 and y == y_1) or (x == x_2 and y == y_2) or (x == x_3 and y == y_3) or (x == x_4 and y == y_4):
            count_corner += 1
        text = pygame.font.Font(None, 100)
        text_wall_count = text.render(str(count_corner), True, color_text)
        screen.blit(text_wall_count, (wight_screen // 2 + 10, height_screen - 75))

        if (x == x_1 and not y == y_1) or (x == x_1 and not y == y_3) or \
                (x == x_2 and not y == y_4) or (x == x_2 and not y == y_2) or \
                (y == y_1 and not x == x_1) or (y == y_1 and not x == x_4) or \
                (y == y_2 and not x == x_2) or (y == y_2 and not x == x_3):
            count_wall += 1
            if f == 1 and ((y == y_2 and not x == x_2) or (y == y_2 and not x == x_3)):
                count_wall -= 1
        text = pygame.font.Font(None, 100)
        text_wall_count = text.render(str(count_wall), True, color_text)
        screen.blit(text_wall_count, (wight_screen // 2 - 300, height_screen - 75))

        # смена цвета линии
        pygame.draw.rect(screen_1, color, ((wight_screen - 100, height_screen - 100), (100, 100)))
        pygame.draw.rect(screen_1, (0, 0, 0), ((wight_screen - 100, height_screen - 100), (100, 100)), 1)
        text = pygame.font.Font(None, 36)
        text_line = text.render('LINE', True, color_text)
        text_color = text.render('COLOR', True, color_text)
        screen.blit(text_line, (wight_screen - 80, height_screen - 75))
        screen.blit(text_color, (wight_screen - 92, height_screen - 40))
        # очистка
        pygame.draw.rect(screen_1, (0, 0, 0), ((wight_screen - 210, height_screen - 100), (100, 100)), 1)
        text_clear = text.render('CLEAR', True, color_text)
        screen_1.blit(text_clear, (wight_screen - 202, height_screen - 57))
        clock = pygame.time.Clock()

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()