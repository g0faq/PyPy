import pygame

if __name__ == '__main__':
    pygame.init()

    # вычисление разрешения экаран
    infoObject = pygame.display.Info()
    wight_screen = infoObject.current_w
    height_screen = infoObject.current_h
    size_screen = (wight_screen, height_screen)

    screen = pygame.display.set_mode(size_screen)
    running = True

    pygame.draw.rect(screen, (255, 255, 255), ((wight_screen // 2 - 205, 45), (410, height_screen - 90)), 10)
    pygame.draw.rect(screen, (255, 0, 255), ((wight_screen // 2 - 200, 50), (400, height_screen - 100)))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()