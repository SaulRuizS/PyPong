#PyPong

#import os
import pygame
from player import Player

#os.environ["SDL_AUDIODRIVER"] = "dummy"

#os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()

clock = pygame.time.Clock()

player_color   = pygame.Color(255,255,255,255) #White
bg_color       = pygame.Color(35,35,35,255) #Gray
player_width   = 30
player_height  = 120

# Set up display
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PyPong")

# Define initial position
p1_x_pos, p1_y_pos = 50, (SCREEN_HEIGHT // 2) - player_height / 2 
p2_x_pos, p2_y_pos = SCREEN_WIDTH - (50 + player_width), (SCREEN_HEIGHT // 2) - player_height / 2

# Step size for movement
speed = 8

playerOne = Player(screen, p1_x_pos, p1_y_pos, SCREEN_WIDTH, SCREEN_HEIGHT, player_color, player_width, player_height)
playerTwo = Player(screen, p2_x_pos, p2_y_pos, SCREEN_WIDTH, SCREEN_HEIGHT, player_color, player_width, player_height)

running = True
while running:

    #Close game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #PlayerOne movement
    playerOne.controller(speed)
    playerTwo.controller(speed)

    # Clear screen and draw updated position
    screen.fill(bg_color)

    #pygame.display.flip()

    clock.tick(60)

pygame.quit()