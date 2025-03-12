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
        self.angle = new_random_angle = self.randomAngle(180)
        print(self.angle)

    def draw(self):
        pygame.draw.circle(self.screen,self.color,(self.x_pos,self.y_pos),self.radius)

    def movement(self,speed,switch,angle):
        #print(math.sin(math.radians(self.angle)))
        self.x_pos = self.x_pos + (switch * speed * math.cos(math.radians(angle)))
        self.y_pos = self.y_pos + (switch * speed * math.sin(math.radians(angle)))

    def randomAngle(self,base_angle):
        new_random_angle = math.floor(random.random() * base_angle)
        return new_random_angle