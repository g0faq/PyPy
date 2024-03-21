import pygame
from random import randrange as rnd

WIDTH, HEIGHT = 1200, 800
FPS = 60

#платформа
paddle_width = 270
paddle_height = 18
paddle_speed = 15
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - paddle_height - 10, paddle_width, paddle_height)

#шарик
ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#кирпичики
#level1
block_list_level_1 = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(3)]
color_list_level_1 = [(rnd(0, 256), rnd(0, 256), rnd(0, 256)) for i in range(10) for j in range(3)]
#level2
block_list_level_2 = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(5)]
color_list_level_2 = [(rnd(0, 256), rnd(0, 256), rnd(0, 256)) for i in range(10) for j in range(5)]
#level3
block_list_level_3 = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(7)]
color_list_level_3 = [(rnd(0, 256), rnd(0, 256), rnd(0, 256)) for i in range(10) for j in range(7)]

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
img = pygame.image.load("new.jpg").convert()

def draw_menu():
    screen.fill('black')
    pygame.display.set_caption('Прямоугольник')
    pygame.draw.rect(screen, 'green', (0, 0,
                                       300, 100))
    pygame.draw.rect(screen, 'blue', (450, 250,
                                      300, 100))
    pygame.draw.rect(screen, 'red', (900, 500,
                                     300, 100))

    font = pygame.font.Font(None, 50)
    text = font.render("LEVEL 1", True, (0, 0, 0))
    text_x_1, text_y_1 = 70, 30
    screen.blit(text, (text_x_1, text_y_1))

    font = pygame.font.Font(None, 50)
    text = font.render("LEVEL 2", True, (0, 0, 0))
    text_x_2, text_y_2 = wight // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2
    screen.blit(text, (text_x_2, text_y_2))

    font = pygame.font.Font(None, 50)
    text = font.render("LEVEL 3", True, (0, 0, 0))
    text_x_3, text_y_3 = 980, 540
    screen.blit(text, (text_x_3, text_y_3))

pygame.init()
try:
    wight, height = 1200, 600
    size = wight, height
    screen = pygame.display.set_mode(size)
    draw_menu()
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
except Exception:
    print('Неправильный формат ввода')

def detect_collusion(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy> 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top
    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = - dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

choice_level, choice_color_level = '', ''
def get_click(mouse_pos):
    global choice_level, choice_color_level
    x, y = mouse_pos
    if 300 > x > 0 and 100 > y > 0:
        choice_level = block_list_level_1
        choice_color_level = color_list_level_1
    if 750 > x > 450 and 350 > y > 250:
        choice_level = block_list_level_2
        choice_color_level = color_list_level_2
    if 1200 > x > 900 and 600 > y > 500:
        choice_level = block_list_level_3
        choice_color_level = color_list_level_3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            get_click(event.pos)

    #шаблон
    sc.blit(img, (0, 0))
    [pygame.draw.rect(sc, color_list_level_1[color], block) for color, block in enumerate(block_list_level_1)]
    pygame.draw.rect(sc, (255, 0, 255), paddle)
    pygame.draw.circle(sc, (255, 255, 255), ball.center, ball_radius)
        #движение шарика
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy
        #левый и правый край
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx
        #верхний край
    if ball.centery < ball_radius:
        dy = -dy
        #столкновение с платформой
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collusion(dx, dy, ball, paddle)
        #столкновение с блоком
    hit_index = ball.collidelist(block_list_level_1)
    if hit_index != -1:
        hit_rect = block_list_level_1.pop(hit_index)
        hit_color = color_list_level_1.pop(hit_index)
        dx, dy = detect_collusion(dx, dy, ball, hit_rect)
    #победа/проигрыш
    if ball.bottom > HEIGHT:
        exit()


    #управление
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed



    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()