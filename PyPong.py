#PyPong

#import os
import pygame
from   player   import Player
from   ball     import Ball
from   field    import Field

#os.environ["SDL_AUDIODRIVER"] = "dummy"

#os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()

clock = pygame.time.Clock()

player_color   = pygame.Color(255,255,255,255) #White
ball_color     = pygame.Color(255,255,255,255) #White
field_color    = pygame.Color(100,100,100,100) #Light Gray
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

ball_x_pos, ball_y_pos = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
ball_radius = 10

field_width = 10

# Step size for movement
speed = 8

playerOne = Player(screen, p1_x_pos, p1_y_pos, SCREEN_WIDTH, SCREEN_HEIGHT, player_color, player_width, player_height)
playerTwo = Player(screen, p2_x_pos, p2_y_pos, SCREEN_WIDTH, SCREEN_HEIGHT, player_color, player_width, player_height)

ball = Ball(screen,ball_color,ball_x_pos,ball_y_pos,ball_radius)

field = Field(screen,field_color)

ball_speed = 7

ball_switch = 1

new_ball_angle = ball.angle

player_one_score = 0
player_two_score = 0

def ballBordersBehavior():
    global ball_switch
    global new_ball_angle

    if ball.x_pos - ball_radius < playerOne.x_pos + player_width and ball.x_pos - ball_radius > playerOne.x_pos - 2:
        if playerOne.y_pos < ball.y_pos - ball_radius and playerOne.y_pos + player_height > ball.y_pos + ball_radius:
            ball_switch *= -1
            new_ball_angle = 0 - (new_ball_angle + ball.randomAngle())
            print(ball_switch)
            print(new_ball_angle)  

    if ball.x_pos + ball_radius > playerTwo.x_pos:
        ball_switch *= -1
        new_ball_angle = 0 - new_ball_angle
        print(ball_switch)
        print(new_ball_angle)

    if ball.y_pos - ball_radius < 0 + field_width or ball.y_pos + ball_radius > SCREEN_HEIGHT - field_width:
        ball_switch *= -1
        new_ball_angle = 180 - new_ball_angle
        print(ball_switch)
        print(new_ball_angle)

    ball.movement(ball_speed,ball_switch,new_ball_angle)
    ball.draw()

def scoreUpdate():
    global player_one_score
    global player_two_score

    if ball.x_pos == 0:
        player_two_score += 1
        print('Player 2 Score:' + str(player_two_score))
        
    elif ball.x_pos == SCREEN_WIDTH:
        player_one_score += 1
        print('Player 1 Score:' + str(player_one_score))
    

running = True
while running:

    #Close game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen and draw updated position
    screen.fill(bg_color)

    #Midfield line
    field.drawMidField(SCREEN_WIDTH/2,0,SCREEN_WIDTH/2,SCREEN_HEIGHT,3)
    
    #Borders
    field.drawBorder(0,0,field_width,SCREEN_WIDTH)
    field.drawBorder(0,SCREEN_HEIGHT-field_width,field_width,SCREEN_WIDTH)

    #PlayerOne movement
    playerOne.controller(speed)
    
    #PlayerTwo movement
    playerTwo.draw()

    #Ball upper and lower limits
    ballBordersBehavior()

    #Ball-Player behavior
    #ballPlayerBehavior()

    #scoreUpdate()

    #pygame.display.flip()
    pygame.display.update()

    clock.tick(60)

pygame.quit()