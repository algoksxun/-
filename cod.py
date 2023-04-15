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
        
bg = img("bg.png", 0,0,800,600)
car = img("car.png", 0,0,400,150)
car2 = img("carpovorot.png", 0,0,400,150)
kamen = img("kamen.png", 300,350,200,150)

carga = random.randint(1,3)


carx = 800
cary = 400

car1x = -400
car1y = 400

sc = pygame.display.set_mode((800, 600)) 
clk = pygame.time.Clock()
clk.tick(60)
game = True 
while game:
    for i in pygame.event.get(): 
        if i.type == pygame.QUIT: 
            game = False

    bg.draw(0,0)
    kamen.draw(300,425)

    
    if carga == 1:
        carx -=10
        print(carx)
        if carx <= -400:
            carx = 900
            carga = random.randint(1,2)


    if carga == 2:
        car1x +=10
        print(car1x)
        if car1x >= 800:
            car1x = -500
            carga = random.randint(1,2)

    car.draw(carx,cary)
    car2.draw(car1x,car1y)


    clk.tick(60)
    pygame.display.update()

pygame.QUIT
