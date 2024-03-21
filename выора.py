import pygame
import random

if __name__ == '__main__':
    pygame.init()

    running = True
    xy = (600, 200)
    xy_copy = xy

    screen = pygame.display.set_mode((800, 300))
    screen.fill('white')

    flag = False
    flag_true = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            x_mouse = pygame.mouse.get_pos()[0]
            y_mouse = pygame.mouse.get_pos()[1]
            if (x_mouse > xy[0]) and (x_mouse < xy[0] + 200) and (y_mouse > xy[1]) and (y_mouse < xy[1] + 100):
                while not flag:
                    x1, y1 = random.randint(0, 601), random.randint(0, 201)
                    if (x1 < 200 and y1 > 200) or (y1 + 100 > 200):
                        flag = False
                    else:
                        flag = True
                xy_copy = xy
                xy = (x1, y1)
                flag = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (x_mouse < 200) and (y_mouse > 200):
                    flag_true = True
                    pygame.draw.rect(screen, (255, 255, 255), ((0, 200), (200, 100)))
                    text = pygame.font.Font(None, 50)
                    text_yes = text.render('я так и знал', True, (0, 0, 0))
                    screen.blit(text_yes, (20, 250))

            if not flag_true:
                pygame.draw.rect(screen, (0, 255, 0), ((0, 200), (200, 100)))
            pygame.draw.rect(screen, (255, 255, 255), ((xy_copy[0], xy_copy[1]), (200, 100)))
            text = pygame.font.Font(None, 70)
            text = text.render('гриша, ты гей?', True, (0, 0, 0))
            screen.blit(text, (250, 25))
            pygame.draw.rect(screen, (255, 0, 0), ((xy[0], xy[1]), (200, 100)))

        pygame.display.flip()
    pygame.quit()