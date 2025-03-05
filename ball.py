#Ball

import pygame
import math
import random

class Ball:

    def __init__(self,screen,color,x_pos,y_pos,radius):
        self.screen = screen
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.angle = math.floor(random.random() * 360)
        print(self.angle)

    def draw(self):
        pygame.draw.circle(self.screen,self.color,(self.x_pos,self.y_pos),self.radius)

    def movement(self,speed,switch):

        #print(math.sin(math.radians(self.angle)))
        if switch == 1:  
            self.x_pos -= speed * math.cos(math.radians(self.angle))
            self.y_pos -= speed * math.sin(math.radians(self.angle))
        else:
            self.x_pos += speed * math.cos(math.radians(180 - self.angle))
            self.y_pos += speed * math.sin(math.radians(180 - self.angle))
    