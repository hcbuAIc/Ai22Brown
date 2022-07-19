import pygame
import numpy as np
import random
import time

SIZE = np.array((800,800))
screen = pygame.display.set_mode(SIZE)

run = True
delta = 0

objects = []
colorOptions = ((1,0,0),(0,1,0.2),(0,0.4,1),(1,0.6,0),(0.6,0,1))
def Normalize(a):

    mag = np.linalg.norm(a)
    if (mag == 0):
        return a
    return a/mag
class Ball():

    def __init__(self):
        
        global objects

        objects.append(self)

        self.color = np.array((255,255,255)) * np.array(random.choice(colorOptions))

        self.radius = random.randint(6,12)
        self.position = np.array((random.randint(self.radius,SIZE[0]-self.radius) + 0.0,0.0 + random.randint(self.radius,SIZE[1]-self.radius)))
        self.velocity = Normalize(np.array((0.0+random.randint(-100,100)/100,0.0+random.randint(-100,100)/100)))

    def update(self):

        self.position += self.velocity * delta * 50
        if (self.position[0] > SIZE[0]-self.radius):
            self.position[0] = SIZE[0]-self.radius
            self.velocity *= np.array((-1,1))
        if (self.position[0] < self.radius):
            self.position[0] = self.radius
            self.velocity *= np.array((-1,1))

        if (self.position[1] > SIZE[1]-self.radius):
            self.position[1] = SIZE[1]-self.radius
            self.velocity *= np.array((1,-1))
        if (self.position[1] < self.radius):
            self.position[1] = self.radius
            self.velocity *= np.array((1,-1))

        pygame.draw.circle(screen,self.color,self.position,self.radius)
lTime = time.time()

for i in range(30):
    b = Ball()
while (run):

    delta = time.time()-lTime
    lTime = time.time()
    screen.fill((255,255,255))

    for object in objects:
        object.update()

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False
    pygame.display.update()
    pygame.display.flip()
pygame.quit()