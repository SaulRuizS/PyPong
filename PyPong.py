#PyPong

#import os
import pygame

#os.environ["SDL_AUDIODRIVER"] = "dummy"

#os.environ["SDL_VIDEODRIVER"] = "dummy"

screen_width    = 1280
screen_height   = 720
posX            = screen_width/2
posY            = screen_height/2
rect_height     = 100
rect_width      = 200

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
running = True

bg_color = pygame.Color(255,255,255,255)

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")

    #pygame.draw.circle(screen,bg_color,(640,360),200,5)

    #pygame.draw.rect(screen,bg_color,pygame.Rect(posX-rect_width/2,posY-rect_height/2,rect_width,rect_height))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()