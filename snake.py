import pygame
import score

pygame.init()

# Values
snake_w = 300
snake_height = 300
game_over = False
size = 15
speed = 0.5
velocity_x = 0
velocity_y = 0

# Colors
black = (0, 0, 0)

snake_length = 1
snake_list = []


def SnakeBody(screen):
    for x, y in snake_list:
        pygame.draw.rect(screen, black, (x, y, size, size))


def SnakeMovement():
    global snake_w, snake_height, velocity_x, velocity_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        velocity_x, velocity_y = -speed, 0
    elif keys[pygame.K_RIGHT]:
        velocity_x, velocity_y = speed, 0
    elif keys[pygame.K_UP]:
        velocity_x, velocity_y = 0, -speed
    elif keys[pygame.K_DOWN]:
        velocity_x, velocity_y = 0, speed

    snake_w += velocity_x
    snake_height += velocity_y
    snake_list.append([snake_w, snake_height])

    if len(snake_list) > snake_length:
        snake_list.pop(0)


def SnakeDead():
    global game_over, snake_w, snake_height, velocity_x, velocity_y, size, speed, snake_length
    snake_head = snake_list[-1]
    if (snake_w < 0 or snake_w >= 800 or snake_height < 0 or snake_height >= 600 or
            snake_head in snake_list[:-1]):
        # pygame.mixer.Sound('Audio/Wood Hit Metal Crash.mp3').play()
        # pygame.time.delay(1000)
        game_over = False
        snake_w, snake_height = 300, 300
        size, speed = 10, 0.2
        score.score = 0
        velocity_x, velocity_y = 0, 0
        snake_length = 1
        snake_list.clear()


def IncreaseSnakeLength():
    global snake_length
    snake_length += 20

