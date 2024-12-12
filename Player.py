import math
import pygame
import neuralnet as nn



class Player():
    def __init__(self, brain):
        pygame.sprite.Sprite.__init__(self)
        self.playerRight = pygame.transform.scale(pygame.image.load("assets/right.png"), (80,80)).convert_alpha()        # Facing Right
        self.playerRight_1 = pygame.transform.scale(pygame.image.load("assets/rightSit.png"), (80,80)).convert_alpha()   # Facing Right while launching
        self.playerLeft = pygame.transform.scale(pygame.image.load("assets/left.png"), (80,80)).convert_alpha()         # Facing Left
        self.playerLeft_1 = pygame.transform.scale(pygame.image.load("assets/leftSit.png"), (80,80)).convert_alpha()     # Facing Left while launching
        self.x = 300            # Current X position
        self.y = 550              # Current Y position
        self.startY = 300
        self.direction = 0          # direction facing; 0 is right; 1 is left
        self.xvel = 0
        self.brain = brain
        self.jump = 0
        self.gravity = 0
        self.ai = True
        self.fitness = 0

    
    def move(self, decision):

        if self.jump == 0:        
            self.gravity += 0.5
            self.y += self.gravity
            self.startY -= self.gravity

        elif self.jump > 0:
            self.jump -= 1
            self.y -= self.jump
            
            self.startY += self.jump

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if (self.ai == True):
                self.ai = False
            else:
                self.ai = True

        if (self.ai == True):
            if (decision == 0):
                if self.xvel < 10:
                    self.xvel += 1
                    self.direction = 0

            elif (decision == 1):
                if self.xvel > -10:
                    self.xvel -= 1
                self.direction = 1
            elif (decision == 2):
                if self.xvel > 0:
                    self.xvel -= 1
                elif self.xvel < 0:
                    self.xvel += 1
        else:
            if key[pygame.K_RIGHT]:
                if self.xvel < 10:
                    self.xvel += 1
                    self.direction = 0

            elif key[pygame.K_LEFT]:
                if self.xvel > -10:
                    self.xvel -= 1
                self.direction = 1
            else:
                if self.xvel > 0:
                    self.xvel -= 1
                elif self.xvel < 0:
                    self.xvel += 1
        
        self.x += self.xvel
        
        # When at the edge of the screen go to the other side
        if self.x > 650:
            self.x = -50
        elif self.x < -50:
            self.x = 650
    
    # Ai Part
    def think(self, platforms):
        '''From input array before sending data to neural network'''
        coordinatesUp = self.getPlatformAbove(platforms)
        coordinatesDown = self.getPlatformBelow(platforms)
        inputs = []
        vision = self.look(platforms)
        # left, right, down vision
        inputs.append(vision[0])
        inputs.append(vision[1])
        inputs.append(vision[2])
        # platform distances
        inputs.append(coordinatesUp - self.x/600-self.x)
        inputs.append(coordinatesDown - self.x/600 -self.x)
        
        output = self.brain.feedForward(inputs).tolist()     
        # choose the option with the highest probability
        index = output.index(max(output))
        return index

    def getPlatformAbove(self,platforms):
        '''Retrieve X value of platform above player'''
        for p in platforms:
            if (self.startY < p.startY):
                if (p.kind != 2):
                    return p.x
            
    def getPlatformBelow(self,platforms):
        '''Retrieve X value of platform below player'''
        maxX = 0
        for p in platforms:
            if (self.startY > p.startY):
                if (p.kind != 2):
                    maxX = p.x
        return maxX

    def fitnessExpo(self):
        self.fitness = self.fitness**2

    def look(self, platforms):
        '''Look for platforms in 3 directions'''
        vision = [0, 0, 0]
        down = pygame.Rect(self.x + 50, self.y-800, 1, 800)
        left = pygame.Rect(self.x-600, self.y +50, 600, 1)
        right = pygame.Rect(self.x, self.y +50, 600, 1)

        for p in platforms:
            # Create a hitbox for the platform
            rect = pygame.Rect(p.x , p.y, p.green.get_width(), p.green.get_height())
            
            if (rect.colliderect(down) and p.kind != 2):
                vision[0] = 1

            elif (rect.colliderect(left) and p.kind != 2):
                vision[1] = 1

            elif (rect.colliderect(right) and p.kind != 2):
                vision[2] = 1

        return vision

    def clone(self):
        cloneBrain = self.brain.clone()
        clone = Player(cloneBrain)
        return clone
