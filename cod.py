import pygame 
import time 
import random

pygame.init() 
pygame.font.init() 
 
class img: 
 
    def __init__(self, file_name, x, y, width, height): 
        self.image = pygame.image.load(file_name) 
        self.newimage = pygame.transform.scale(self.image, (width, height)) 
 
    def draw(self, x, y): 
        sc.blit(self.newimage, (x, y)) 
 
    def collidepoint(self, x, y): 
        return self.rect.collidepoint(x, y)
        

sc = pygame.display.set_mode((500, 500)) 
clk = pygame.time.Clock()

game = True 
while game:
    for i in pygame.event.get(): 
        if i.type == pygame.QUIT: 
            game = False
