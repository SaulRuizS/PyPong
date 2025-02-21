#Ball

import pygame

class Ball:
    def __init__(self,screen,color,x_pos,y_pos,radius):
        self.screen = screen
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.screen,self.color,(self.x_pos,self.y_pos),self.radius)