#Controller

import pygame

class Player:
    def __init__(self,screen,x_pos,y_pos,max_width,max_height,color,player_width,player_height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.max_width = max_width
        self.max_height = max_height
        self.screen = screen
        self.color = color
        self.player_width = player_width
        self.player_height = player_height

    def draw(self):
        #Draw player
        pygame.draw.rect(self.screen,self.color,pygame.Rect(self.x_pos,self.y_pos,self.player_width,self.player_height))

    def controller(self,speed):
        #Get keys pressed
        keys = pygame.key.get_pressed()

        #if self.y_pos > 0 and (self.y_pos + self.player_height) < self.max_height:
        if keys[pygame.K_UP] and self.y_pos > 0:
            self.y_pos -= speed
        if keys[pygame.K_DOWN] and self.y_pos < self.max_height - self.player_height:
            self.y_pos += speed

        self.draw()

    def verticalMovement(self,direction,speed):
        if direction == -1:
            self.y_pos -= speed
        if direction == 1:
            self.y_pos += speed

        #self.draw()