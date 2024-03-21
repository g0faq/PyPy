import pygame

def draw(w, hue):
    screen.fill('black')
    pygame.display.set_caption('Куб')
    left = (300 - (w + w // 2)) // 2
    top = (300 - (w + w // 2)) // 2 + w // 2
    color = pygame.Color(hue[0], hue[1], hue[2])
    pygame.draw.polygon(screen, color, [[left, top],
                                        [left + w // 2, top - w // 2],
                                        [left + w + w // 2, top - w // 2],
                                        [left + w, top]])

    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], int(hsv[2] * 0.75), hsv[3])
    pygame.draw.rect(screen, color, (left, top, w, w))

    color.hsva = (hsv[0], hsv[1], int(hsv[2] * 0.5), hsv[3])
    pygame.draw.polygon(screen, color, [[left + w + w // 2, top - w // 2],
                                        [left + w, top],
                                        [left + w, top + w],
                                        [left + w + w // 2, top + w // 2]])

pygame.init()
try:
    w, *hue = map(int, input().split())
except Exception:
    print('Неправильный формат ввода')
wight, height = 300, 300
size = wight, height
screen = pygame.display.set_mode(size)
draw(w, hue)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()