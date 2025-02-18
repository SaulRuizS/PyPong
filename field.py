#Field

import pygame

class Field:
    def __init__(self,screen,color):
        self.screen = screen
        self.color = color

    def drawMidField(self,init_x_pos,init_y_pos,end_x_pos,end_y_pos,width):
        pygame.draw.line(self.screen,self.color,(init_x_pos,init_y_pos),(end_x_pos,end_y_pos),width)
        pygame.display.update()

    def drawBorder(self,x_pos,y_pos,height,width):
        pygame.draw.rect(self.screen,self.color,pygame.Rect(x_pos,y_pos,width,height))
        pygame.display.update()