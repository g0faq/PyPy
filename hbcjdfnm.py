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

    mouse_in_break = (255, 0, 0)
    mouse_in_rect = (0, 0, 255)
    mouse_in_circle = (0, 0, 255)

    mouse_in_rect_flag = False
    mouse_in_circle_flag = False

    # заливка экрана
    screen.fill((0, 0, 0))

    list_mousebutton = []
    line_count = 0
    rect = False
    circle = False

    wight = 200
    height = 100

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
            if (x_mouse < 100) and (y_mouse > height_screen - 100):
                mouse_in_rect = (0, 0, 255)
            else:
                mouse_in_rect = (0, 0, 215)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (x_mouse > wight_screen - 100) and (y_mouse < 100):
                    running = False
                else:
                    list_mousebutton.append((x_mouse, y_mouse))
                    line_count += 1
                if (x_mouse < 100) and (y_mouse > height_screen - 100):
                    if not mouse_in_rect_flag:
                        mouse_in_rect_flag = True
                    else:
                        mouse_in_rect_flag = False

        if not mouse_in_rect_flag and not mouse_in_circle_flag:
            if len(list_mousebutton) > 1:
                pygame.draw.line(screen, (255, 0, 255), (list_mousebutton[line_count - 2]), (list_mousebutton[line_count - 1]))

        if mouse_in_rect_flag:
            pygame.draw.rect(screen, (255, 0, 255), (list_mousebutton[line_count - 1], (list_mousebutton[line_count])))

        pygame.draw.line(screen, mouse_in_break, (wight_screen - 80, 20), (wight_screen - 20, 80), 10)
        pygame.draw.line(screen, mouse_in_break, (wight_screen - 20, 20), (wight_screen - 80, 80), 10)

        if mouse_in_rect_flag:
            pygame.draw.rect(screen, (255, 0, 0), ((10, height_screen - 110), (100, 100)))
        else:
            pygame.draw.rect(screen, mouse_in_rect, ((10, height_screen - 110), (100, 100)))

        pygame.display.flip()
    pygame.quit()