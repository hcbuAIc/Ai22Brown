import pygame,math,random,numpy as np,time


SIZE = np.array((800.0,800.0))
screen = pygame.display.set_mode(SIZE)

#loading and scaling the DVD Image
image = pygame.transform.scale(pygame.image.load("Assets/DVD_logo.svg.png"),(80,60))


run = True

#variables needed to calculate time between frames
delta = 0
lTime = time.time()


objects = []
colorOptions = ((1,0,0),(0,1,0.2),(0,0.4,1),(1,0.6,0),(0.6,0,1))

#vector normalization function
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

        self.radius = 30
        self.position = SIZE/2
        self.velocity = Normalize(np.array((0.0+random.randint(-100,100)/100,0.0+random.randint(-100,100)/100)))

    def update(self):

        #Simple collision detection
        self.position += self.velocity * delta * 120
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
        #blit the image to the screen
        screen.blit(image,self.position-np.array((self.radius,self.radius)))


b = Ball()
while (run):

    #delta accounts for the time between frames which allows changes to occur at a rate independant of the framerate
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