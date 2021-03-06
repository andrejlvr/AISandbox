import pygame, sys, math, random
from pygame.locals import *

#game engine init
pygame.init()
fpsClock = pygame.time.Clock()

h = 480
w = 640
#create frame
frame = pygame.display.set_mode((w, h))
pygame.display.set_caption('Pygame sandbox')

#class
class Man(pygame.sprite.Sprite):
    def __init__(self, position, speed, vel):
        pygame.sprite.Sprite.__init__(self)
        self.current_direction = pygame.Surface([17, 32])
        self.standing = pygame.image.load('assets/m_standing.png')
        self.left = pygame.image.load('assets/m_left.png')
        self.walkingLeft = pygame.image.load('assets/m_walking_left.png')
        self.up = pygame.image.load('assets/m_up.png')
        self.walkingUp = pygame.image.load('assets/m_walking_up.png')
        self.down = pygame.image.load('assets/m_down.png')
        self.walkingDown = pygame.image.load('assets/m_walking_down.png')
        self.right = pygame.image.load('assets/m_right.png')
        self.walkingRight = pygame.image.load('assets/m_walking_right.png')

        self.rect = self.current_direction.get_rect()
        self.current_direction = self.standing
        self.current_position = [w/2,h/2]
        self.speed = speed
        self.vel = vel
        self.animation_interval = 25
        self.solve = False

    def updatePosition(self):
        self.current_position[0] += self.vel[0]
        self.current_position[1] += self.vel[1]

    def setVelocity(self, vel):
        #self.vel[0] += vel[0]
        #self.vel[1] += vel[1]
        self.vel[0] = vel[0]
        self.vel[1] = vel[1]

    def getDirection(self):
        if self.vel[0] + self.vel[1] == 0:
            return self.standing
        elif vel[0] < 0:
            if self.current_position[0] % self.animation_interval < self.animation_interval/2:
                return self.walkingLeft
            return self.left
        elif vel[0] > 0:
            if self.current_position[0] % self.animation_interval < self.animation_interval/2:
                return self.walkingRight
            return self.right
        elif vel[1] < 0:
            if self.current_position[1] % self.animation_interval < self.animation_interval/2:
                return self.walkingUp
            return self.up
        elif vel[1] > 0:
            if self.current_position[1] % self.animation_interval < self.animation_interval/2:
                return self.walkingDown
            return self.down

    def getPosition(self):
        return self.current_position

    def stopIt(self):
        self.vel[0] = 0
        self.vel[1] = 0

    def get_rect():
        return self.rect

    def getSpeed(self):
        return self.speed

    def checkCollision(self, destination):
        x = math.fabs(destination[0] - self.current_position[0])
        y = math.fabs(destination[1] - self.current_position[1])
        return (x + y) > 30

    def save(self, destination):
        x = math.fabs(destination[0] - self.current_position[0])
        y = math.fabs(destination[1] - self.current_position[1])

        a = self.current_position[0]
        b = self.current_position[1]     

        print a,destination[0]
        
        if a != destination[0] or x > 50:
            if self.current_position[0] - destination[0] > 0:
                    self.setVelocity([-1 * self.getSpeed(),0])
            else:
                    self.setVelocity([1 * self.getSpeed(),0])
        else:
            if b != destination[1]:
                if self.current_position[1] - destination[1] > 0:
                        self.setVelocity([0,-1 * self.getSpeed()])
                else:
                        self.setVelocity([0,1 * self.getSpeed()])   
    
class Wounded(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.wounded = pygame.Surface([20, 20])
        self.wounded = pygame.image.load('assets/m_wounded.png')
        self.position = [random.randint(0,w),random.randint(0,h)]
        self.rect = self.wounded.get_rect()

    def getPosition(self):
        return self.position

    def getDirection(self):
        return self.wounded

    def get_rect(self):
        return self.rect

    def setPosition(self, new):
        self.position[0] = new[0]
        self.position[1] = new[1]

#constants
white = pygame.Color(255, 255, 255)
rand = [random.randint(0,w),random.randint(0,h)]
vel = [0,0]

man = Man(rand,2,vel)
wounded = Wounded()
wounded2 = Wounded()
wounded3 = Wounded()

while True:
    frame.fill(white)
    man.updatePosition()

    frame.blit(wounded.getDirection(), wounded.getPosition()) 
    frame.blit(man.getDirection(), man.getPosition())

    if man.checkCollision(wounded.getPosition()):
        man.save(wounded.getPosition())
    else:
        #man.stopIt()
        wounded.setPosition([random.randint(0,w),random.randint(0,h)])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP and event.type != KEYDOWN:
            if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                if event.key == K_LEFT:
                    man.setVelocity([1 * man.getSpeed(),0])
                elif event.key == K_RIGHT:
                    man.setVelocity([-1 * man.getSpeed(),0])
                elif event.key == K_UP:
                    man.setVelocity([0,1 * man.getSpeed()])
                elif event.key == K_DOWN:
                    man.setVelocity([0,-1 * man.getSpeed()])
        elif event.type == KEYDOWN:
            if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                if event.key == K_LEFT:
                    man.setVelocity([-1 * man.getSpeed(),0])
                elif event.key == K_RIGHT:
                    man.setVelocity([man.getSpeed(),0])
                elif event.key == K_UP:
                    man.setVelocity([0,-1 * man.getSpeed()])
                elif event.key == K_DOWN:
                    man.setVelocity([0,man.getSpeed()])
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    pygame.display.update()
    fpsClock.tick(30) 
