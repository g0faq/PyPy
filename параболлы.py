import pygame


if __name__ == '__main__':
    pygame.init()

    infoObject = pygame.display.Info()
    wight_screen = infoObject.current_w
    height_screen = infoObject.current_h
    size_screen = (wight_screen, height_screen)
    screen = pygame.display.set_mode(size_screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        step_wight = int(wight_screen / 100)
        step_height = int(height_screen / 100)
        i = 1
        for w in range(0, wight_screen + step_wight, step_wight):
            i += 1
            for h in range(0, height_screen + step_height, step_wight):
                pygame.draw.line(screen, (255, 0, 255), (wight_screen - (step_wight * i), 0), (0, step_height * i))
                break

        i = 1
        for w in range(0, wight_screen + 2 * step_wight, step_wight):
            i += 1
            for h in range(0, height_screen + 2 * step_height, step_wight):
                pygame.draw.line(screen, (255, 0, 255), (step_wight * i, 0), (wight_screen, step_height * i))
                break

        i = 1
        for w in range(0, wight_screen + step_wight, step_wight):
            i += 1
            for h in range(0, height_screen + step_height, step_wight):
                pygame.draw.line(screen, (255, 0, 255), (wight_screen - (step_wight * i), height_screen), (0, height_screen - step_height * i))
                break

        i = 1
        for w in range(0, wight_screen + 2 * step_wight, step_wight):
            i += 1
            for h in range(0, height_screen + 2 * step_height, step_wight):
                pygame.draw.line(screen, (255, 0, 255), (step_wight * i, height_screen), (wight_screen, height_screen - step_height * i))
                break

        pygame.display.flip()
    pygame.quit()