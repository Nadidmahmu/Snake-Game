import pygame
import os

pygame.init()

# Values
score = 0
highest_score = 0

# Font
font = pygame.font.SysFont(None, 30)

# Load highest score from file
def load_highest_score():
    global highest_score
    try:
        with open("highest.txt", "r") as file:
            highest_score = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        highest_score = 0

# Display the current score on the screen
def display_score(screen):
    score_text = font.render(f'{score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

# Display the highest score on the screen
def display_highest_score(screen):
    highest_score_text = font.render(f'Highest: {highest_score}', True, (0, 0, 0))
    screen.blit(highest_score_text, (350, 10))

# Update the highest score if the current score is greater
def update_highest_score():
    global highest_score
    if score > highest_score:
        highest_score = score
        with open("highest.txt", "w") as file:
            file.write(str(highest_score))

load_highest_score()

