#Controller

import pygame

class Player:
    def __init__(self,x_pos,y_pos,width,height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        pygame.draw.circle(screen, (255, 255, 255), (x_pos, y_pos), 10)
    
    def controller(self,speed):
        #Get keys pressed
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     self.x_pos -= speed
        # if keys[pygame.K_RIGHT]:
        #     self.x_pos += speed
        if keys[pygame.K_UP]:
            self.y_pos -= speed
        if keys[pygame.K_DOWN]:
            self.y_pos += speed

        # Keep position within bounds
        # self.x_pos = max(0, min(self.width, self.x_pos))
        self.y_pos = max(0, min(self.height, self.y_pos))

        #Draw circle
        pygame.draw.circle(screen, (255, 255, 255), (self.x_pos, self.y_pos), 10)
        pygame.display.update()



# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arrow Key Controller")

# Define initial position
x_pos, y_pos = WIDTH // 20, HEIGHT // 2

# Step size for movement
speed = 4

playerOne = Player(x_pos, y_pos, WIDTH, HEIGHT)

# Main loop
running = True
while running:
    pygame.time.delay(10)  # Delay for smooth movement
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    playerOne.controller(speed)
    
    # Clear screen and draw updated position
    screen.fill((0, 0, 0))  # Black backgroun

pygame.quit()

