import pygame
import random
import snake
import score

pygame.init()

# values
FOOD_SIZE = 10
FOOD_COLOR = (255, 0, 0)

food_x, food_y = random.randint(50, int(800 / 2)), random.randint(50, int(600 / 2))

def FoodBody(screen):
    pygame.draw.circle(screen, FOOD_COLOR, (food_x, food_y), FOOD_SIZE)

def FoodRespawn():
    global food_x, food_y
    if abs(snake.snake_w - food_x) < FOOD_SIZE and abs(snake.snake_height - food_y) < FOOD_SIZE:
        food_x, food_y = random.randint(FOOD_SIZE, 800 - FOOD_SIZE), random.randint(FOOD_SIZE, 600 - FOOD_SIZE)
        snake.speed += 0.01
        score.score += 10
        snake.IncreaseSnakeLength()

