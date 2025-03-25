#Score

import pygame

class Score:
    def __init__(self,pos_x,pos_y,color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.font = pygame.font.Font(None,24)

    def drawScore(self,current_score):
        self.font.render(current_score,True,self.color,None)