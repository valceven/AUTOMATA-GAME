import pygame
import random

'''
Current State	Timer <= 0	Next State
IDLE (1)	    Yes	        SHIFT (2)
IDLE (1)	    No	        IDLE (1)
SHIFT (2)	    Yes	        ATTACK (3)
SHIFT (2)	    No	        SHIFT (2)
ATTACK (3)	    Yes	        IDLE (1)
ATTACK (3)	    No	        ATTACK (3)
'''

class Boss:
    IDLE = 1
    SHIFT = 2
    ATTACK = 3
    score = 0

    def __init__(self, name):
        self.name = name
        self.position = pygame.Vector2(1200, 360)
        self.radius = 50
        self.timer = 0
        self.set_idle()

    def set_idle(self):
        self.timer = random.randint(1, 4)
        self.state = self.IDLE
        self.score += 1
        
    def set_shift(self):
        self.timer = random.randint(1, 4)
        self.state = self.SHIFT
    
    def set_attack(self):
        self.timer = random.randint(1, 4)
        self.state = self.ATTACK
        

    def update(self, dt):
        self.timer -= dt
        if self.timer <= 0:
            if self.state == self.IDLE:
                self.set_shift()
            elif self.state == self.SHIFT:
                self.set_attack()
            elif self.state == self.ATTACK:
                self.set_idle()
    
    def draw(self, screen):
        if self.state == self.IDLE:
            color = "red" if self.timer <= 1 else "yellow"
        elif self.state == self.ATTACK:
            color = "blue" 
        elif self.state == self.SHIFT:
            color = "blue" if self.timer <= 0.2 else "red"
    
        pygame.draw.circle(screen, color, self.position, self.radius)

