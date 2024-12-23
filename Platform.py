import pygame 
import random

class Platform():

    def __init__ (self):
        self.kind = 0
        self.green = pygame.transform.scale(pygame.image.load("assets/green.png"), (80,25)).convert_alpha()             # Green Platform
        self.blue = pygame.transform.scale(pygame.image.load("assets/blue.png"), (80,25)).convert_alpha()                # Blue Moving Platform
        self.red = pygame.transform.scale(pygame.image.load("assets/red.png"), (80,25)).convert_alpha()                 # Red Fragile Platform
        self.red_1 = pygame.transform.scale(pygame.image.load("assets/redBroken.png"), (80,25)).convert_alpha()         # Red Broken Platform
        self.spring = pygame.transform.scale(pygame.image.load("assets/spring.png"), (25,25)).convert_alpha()           # Spring
        self.spring_1 = pygame.transform.scale(pygame.image.load("assets/spring_1.png"), (25,25)).convert_alpha()        # Spring activated
        self.x  = random.randint(0, 500)
        self.y = 0
        self.startY = -100         # Actual y
        self.broken = False
        self.collider = pygame.Rect(self.x, self.y, self.green.get_width() - 10, self.green.get_height())
        self.hasSpring = False
        self.springActive = False
        self.blueDirection = 0

    def getKind(self, score):
        # Note kind = 0 is green, 1 is blue, 2 is red
        chance = random.randint(0,100)
        if (score < 1500):
            if (chance < 85):                 # 85% chance to get green platform
                self.kind = 0            
            elif (chance < 95):               # 10% chance to get blue 
                self.kind = 1                   
            else:                             # 5% chance to get red
                self.kind = 2  
        elif (score < 2500):
            if (chance < 75):                 # 75% chance to get green platform
                self.kind = 0            
            elif (chance < 95):               # 20% chance to get blue 
                self.kind = 1                   
            else:                             # 5% chance to get red
                self.kind = 2 
        else:
            if (chance < 50):                 # 50% chance to get green platform
                self.kind = 0            
            elif (chance < 90):               # 40% chance to get blue 
                self.kind = 1                   
            else:
                self.kind = 2                   # 10% chance to get red

    def checkSpring(self):
        chance = random.randint(0, 100)
        if (chance > 95 and self.kind == 0):
            self.hasSpring = True

    def blueMovement(self, score):
        x = 0
        if (score < 2500):
            vel = 5
        else:
            vel = 8
                
        if (self.blueDirection > 0):
            x += vel
            self.x += x
            if (self.x >= 600 - self.blue.get_width()):
                self.blueDirection = 0
        else:      
            self.x -= vel
            
            if (self.x <= 0):
                self.blueDirection = 1
