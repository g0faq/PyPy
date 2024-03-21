import random
import pygame

f = True
# нахождение цветов
background_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
color_text = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
color_button = (0, 0, 0)

if __name__ == '__main__':
    pygame.init()
    # вычисление разрешения экаран
    infoObject = pygame.display.Info()
    wight_screen = infoObject.current_w
    height_screen = infoObject.current_h
    size_screen = (wight_screen, height_screen)

    screen = pygame.display.set_mode(size_screen)
    running = True

    # заливка экрана
    screen.fill(background_color)

    wight = 200
    height = 100

    mouse_in_break = (255, 0, 0)

    # цвета кнопок минус и плюс
    color_wight_minus = (255, 0, 0)
    color_height_minus = (255, 0, 0)
    color_wight_plus = (0, 0, 255)
    color_height_plus = (0, 0, 255)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            x_mouse = pygame.mouse.get_pos()[0]
            y_mouse = pygame.mouse.get_pos()[1]
            if (x_mouse > wight_screen - 100) and (y_mouse < 100):
                mouse_in_break = (255, 0, 0)
            else:
                mouse_in_break = (215, 0, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # ширина -
                if (x_mouse > 450) and (x_mouse < 550) and (y_mouse > 125) and (y_mouse < 225):
                    if wight > 200:
                        wight -= 100
                        color_wight_minus = (0, 0, 255)
                        color_wight_plus = (0, 0, 255)
                    else:
                        color_wight_minus = (255, 0, 0)
                # высота -
                if (x_mouse > 450) and (x_mouse < 550) and (y_mouse > height_screen - 225) and (y_mouse < height_screen - 125):
                    if height > 100:
                        height -= 100
                        color_height_minus = (0, 0, 255)
                        color_height_plus = (0, 0, 255)
                    else:
                        color_height_minus = (255, 0, 0)
                # ширина +
                if (x_mouse > 950) and (x_mouse < 1050) and (y_mouse > 125) and (y_mouse < 225):
                    if wight + 100 < wight_screen - 110:
                        wight += 100
                        color_wight_plus = (0, 0, 255)
                        color_wight_minus = (0, 0, 255)
                    else:
                        color_wight_plus = (255, 0, 0)
                # высота +
                if (x_mouse > 950) and (x_mouse < 1050) and (y_mouse > height_screen - 225) and (y_mouse < height_screen - 125):
                    if height + 100 < height_screen:
                        height += 100
                        color_height_plus = (0, 0, 255)
                        color_height_minus = (0, 0, 255)
                    else:
                        color_height_plus = (255, 0, 0)
                # закрытие программы
                if (x_mouse > wight_screen - 100) and (y_mouse < 100):
                    running = False
                # смена цвета фона
                if (x_mouse > wight_screen - 100) and (y_mouse > height_screen - 100):
                    background_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                    screen.fill(background_color)
                # смена цвета текста
                if (x_mouse < wight_screen - 100) and (x_mouse > wight_screen - 200) and (y_mouse > height_screen - 100):
                    color_text = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                # кнопка старт
                if ((x_mouse > wight_screen - 300) and (x_mouse < wight_screen - 10) and
                    (y_mouse < (height_screen // 2) - 100) and (y_mouse > (height_screen // 2) - 150)):
                    start_flag = True

            # смена цвета кнопок
            if wight == 200:
                color_wight_minus = (255, 0, 0)
            if wight + 100 >= wight_screen - 110:
                color_wight_plus = (255, 0, 0)
            if height == 100:
                color_height_minus = (255, 0, 0)
            if height + 100 >= height_screen:
                color_height_plus = (255, 0, 0)
        if f:
            # шаблон для текста (ширина/высота)
            pygame.draw.rect(screen, color_button, ((100, 100), (300, 150)))
            pygame.draw.rect(screen, color_button, ((100, height_screen - 250), (300, 150)))

            # текст
            text = pygame.font.Font(None, 70)
            text_wight = text.render('ШИРИНА', True, color_text)
            text_height = text.render('ВЫСОТА', True, color_text)
            screen.blit(text_wight, (130, 150))
            screen.blit(text_height, (135, height_screen - 200))

            # кнопки для минусов
            pygame.draw.rect(screen, color_button, ((450, 125), (100, 100)))
            pygame.draw.rect(screen, color_button, ((450, height_screen - 225), (100, 100)))

            # шаблон для выводы ширины/высоты
            pygame.draw.rect(screen, color_button, ((600, 100), (300, 150)))
            pygame.draw.rect(screen, color_button, ((600, height_screen - 250), (300, 150)))

            # кнопки для плюсов
            pygame.draw.rect(screen, color_button, ((950, 125), (100, 100)))
            pygame.draw.rect(screen, color_button, ((950, height_screen - 225), (100, 100)))

            # текст
            text_1 = pygame.font.Font(None, 150)
            text_plus_wight = text_1.render('+', True, color_wight_plus)
            text_minus_wight = text_1.render('-', True, color_wight_minus)
            text_plus_height = text_1.render('+', True, color_height_plus)
            text_minus_height = text_1.render('-', True, color_height_minus)
            text_count_wight = text.render(str(wight), True, color_text)
            text_count_height = text.render(str(height), True, color_text)
            screen.blit(text_plus_wight, (970, 115))
            screen.blit(text_plus_height, (970, height_screen - 235))
            screen.blit(text_minus_wight, (480, 120))
            screen.blit(text_minus_height, (480, height_screen - 230))
            screen.blit(text_count_wight, (690, 150))
            screen.blit(text_count_height, (690, height_screen - 200))

            # кнопка старт
            pygame.draw.rect(screen, color_button, ((wight_screen - 300, height_screen // 2 - 150), (290, 150)))
            text_start = text.render('START', True, (0, 255, 0))
            screen.blit(text_start, (wight_screen - 225, height_screen // 2 - 100))

            # крест
            pygame.draw.line(screen, mouse_in_break, (wight_screen - 80, 20), (wight_screen - 20, 80), 10)
            pygame.draw.line(screen, mouse_in_break, (wight_screen - 20, 20), (wight_screen - 80, 80), 10)

            # кнопки смены цветов
            pygame.draw.rect(screen, (0, 0, 0), ((wight_screen - 200, height_screen - 90), (200, 90)))
            pygame.draw.line(screen, background_color, (wight_screen, height_screen - 100),
                             (wight_screen, height_screen), 10)
            pygame.draw.line(screen, background_color, (wight_screen - 100, height_screen - 100),
                             (wight_screen - 100, height_screen), 10)
            pygame.draw.line(screen, background_color, (wight_screen - 200, height_screen - 100),
                             (wight_screen - 200, height_screen), 10)
            text_color_change = pygame.font.Font(None, 36)
            texts_color = text_color_change.render('COLOR', True, color_text)
            text_color_fond = text_color_change.render('FOND', True, color_text)
            text_color = text_color_change.render('TEXT', True, color_text)
            screen.blit(text_color_fond, (wight_screen - 85, height_screen - 75))
            screen.blit(texts_color, (wight_screen - 92, height_screen - 40))
            screen.blit(text_color, (wight_screen - 185, height_screen - 75))
            screen.blit(texts_color, (wight_screen - 192, height_screen - 40))

        pygame.display.flip()
    pygame.quit()