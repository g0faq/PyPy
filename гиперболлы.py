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

        step_wight = 2
        step_height = 2
        middle = []
        wight = []

        for i in range(height_screen):
            middle.append((int(step_wight * i), int(step_height * i)))
            wight.append(int(step_wight * i))
        for w in range(height_screen):
            pygame.draw.line(screen, (255, 0, 255), (height_screen - wight[w], 0), middle[w])
        for w in range(height_screen):
            pygame.draw.line(screen, (255, 0, 255), (height_screen - wight[w], height_screen), middle[w])
        pygame.display.flip()
    pygame.quit()