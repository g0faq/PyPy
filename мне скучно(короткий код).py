import pygame
import random

if __name__ == '__main__':
    pygame.init()
    background_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
    text_colors = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
    pause_color = (0, 0, 255)
    infoObject = pygame.display.Info()
    wight_screen, height_screen = infoObject.current_w, infoObject.current_h
    size_screen = (wight_screen, height_screen)
    print('Введите желаемую ширину и высоту')
    print('К сожалению ввод одинаковой ширины и высоты запрещён')
    input_wight, input_height = int(input(f'ширина(50-{wight_screen - 110}):')), int(input(f'высота(50-{height_screen}):'))
    input_flag = False
    wight_field, height_field = 0, 0
    if (input_wight <= (wight_screen - 110)) and (input_height <= height_screen) and\
            (input_wight >= 50) and (input_height >= 50) and input_wight != input_height:
        print('Спасибо!')
        input_flag = True
        wight_field, height_field = input_wight, input_height
    else:
        while not input_flag:
            print('Пожалуйста, введите допустимые значения')
            print(f'Ширина от 50 до {wight_screen - 110}')
            print(f'Высота от 50 до {height_screen}')
            input_wight, input_height = int(input(f'ширина(50-{wight_screen-110}):')), int(input(f'высота(50-{height_screen}):'))
            if (input_wight <= (wight_screen - 110)) and (input_height <= height_screen) and \
                    (input_wight >= 50) and (input_height >= 50):
                print('Спасибо!')
                input_flag = True
                wight_field, height_field = input_wight, input_height
    x_1, y_1 = int((wight_screen - wight_field - 100) // 2), int((height_screen - height_field) // 2)
    xy_1 = (x_1, y_1)
    x_2, y_2 = int(x_1 + wight_field), int(y_1 + height_field)
    xy_2 = (x_2, y_2)
    x_3, y_3 = x_1, y_2
    xy_3 = (x_3, y_3)
    x_4, y_4 = x_2, y_1
    xy_4 = (x_4, y_4)
    x, y = x_1, random.randint(y_1, y_3)
    xy_line = (x, y)
    f = 1
    color = (255, 255, 255)
    if input_flag:
        screen, screen_2 = pygame.display.set_mode(size_screen), pygame.display.set_mode(size_screen)
        screen.fill(background_color)
        pygame.draw.polygon(screen, (0, 0, 0), ((x_1, y_1), (x_3, y_3), (x_2, y_2), (x_4, y_4)))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x_mouse, y_mouse = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                    if x_mouse > wight_screen - 100 and y_mouse < 100:
                        if pause_color == (0, 0, 255):
                            pause_color = (255, 0, 0)
                        else:
                            pause_color = (0, 0, 255)
                    if (x_mouse > wight_screen - 100) and (y_mouse > 100) and (y_mouse < 200):
                        color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                    if (x_mouse > wight_screen - 100) and (y_mouse > 300):
                        running = False
                    if (x_mouse > wight_screen - 100) and (y_mouse > 200) and (y_mouse < 300):
                        pygame.draw.polygon(screen, (0, 0, 0), ((x_1, y_1), (x_3, y_3), (x_2, y_2), (x_4, y_4)))
            screen = screen_2
            if pause_color == (0, 0, 255):
                if x < x_1 or x > x_2 or y < y_1 or y > y_2:
                    running = False
                    print('Произошла техничская проблема')
                if ((x == x_1 and y == y_1) or (x == x_2 and y == y_2) or
                        (x == x_1 and y == y_2) or (x == x_2 and y == y_1)):
                    f = 3 if f == 1 else None
                    f = 4 if f == 2 else None
                    f = 1 if f == 3 else None
                    f = 2 if f == 4 else None
                if x == x_2:
                    if f == 2:
                        x, y, f, xy_line = x - 1, y - 1, 1, (x, y)
                    elif f == 3:
                        x, y, f, xy_line = x - 1, y + 1, 4, (x, y)
                elif x == x_1:
                    if f == 4:
                        x, y, f, xy_line = x + 1, y + 1, 3, (x, y)
                    elif f == 1:
                        x, y, f, xy_line = x - 1, y - 1, 2, (x, y)
                elif y == y_2:
                    if f == 3:
                        x, y, f, xy_line = x + 1, y - 1, 2, (x, y)
                    elif f == 4:
                        x, y, f, xy_line = x - 1, y + 1, 1, (x, y)
                elif y == y_1:
                    if f == 1:
                        x, y, f, xy_line = x - 1, y + 1, 4, (x, y)
                    elif f == 2:
                        x, y, f, xy_line = x + 1, y + 1, 3, (x, y)
                if f == 1:
                    x, y = x - 1, y - 1
                elif f == 2:
                    x, y = x + 1, y - 1
                elif f == 3:
                    x, y = x + 1, y + 1
                elif f == 4:
                    x, y = x - 1, y + 1
                pygame.draw.line(screen, color, xy_line, (x, y), 1)
            pygame.draw.polygon(screen, (255, 255, 255), ((x_1 - 5, y_1 - 5), (x_4 + 5, y_4 - 5), (x_2 + 5, y_2 + 5), (x_3 - 5, y_3 + 5)), 10)
            pygame.draw.polygon(screen, (0, 0, 0), ((wight_screen - 100, 0), (wight_screen - 100, 400),
                                (wight_screen, 400), (wight_screen, 0)))
            pygame.draw.polygon(screen, color, ((wight_screen - 100, 100), (wight_screen - 100, 200),
                                (wight_screen, 200), (wight_screen, 100)))
            pygame.draw.line(screen, background_color, (wight_screen - 100, 100), (wight_screen, 100), 10)
            pygame.draw.line(screen, background_color, (wight_screen - 100, 200), (wight_screen, 200), 10)
            pygame.draw.line(screen, background_color, (wight_screen - 100, 300), (wight_screen, 300), 10)
            pygame.draw.line(screen, (255, 0, 0), (wight_screen - 80, 320), (wight_screen - 20, 380), 10)
            pygame.draw.line(screen, (255, 0, 0), (wight_screen - 20, 320), (wight_screen - 80, 380), 10)
            pygame.draw.line(screen, pause_color, (wight_screen - 70, 20), (wight_screen - 70, 80), 20)
            pygame.draw.line(screen, pause_color, (wight_screen - 30, 20), (wight_screen - 30, 80), 20)
            text = pygame.font.Font(None, 36)
            text_line, text_color, text_clear = text.render('LINE', True, text_colors),\
                                                text.render('COLOR', True, text_colors), text.render('CLEAR', True, text_colors)
            screen.blit(text_line, (wight_screen - 90, 130))
            screen.blit(text_color, (wight_screen - 90, 150))
            screen.blit(text_clear, (wight_screen - 90, 240))
            pygame.display.flip()
    pygame.quit()