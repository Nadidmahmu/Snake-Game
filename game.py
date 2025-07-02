import pygame
import os
import random
import snake
import food
import score

pygame.init()

# Values
width, height = 800, 600
exit_game = False
game_over = False

# Colors
colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}

# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

def gameLoop():
    global exit_game
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

        screen.fill(colors['white'])
        snake.SnakeBody(screen)
        snake.SnakeMovement()
        snake.SnakeDead()
        food.FoodBody(screen)
        food.FoodRespawn()
        score.display_score(screen)
        score.display_highest_score(screen)
        score.update_highest_score()
        
        pygame.display.update()
gameLoop()
pygame.quit()

