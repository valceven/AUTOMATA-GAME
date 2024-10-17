import pygame
import random

class Boss:
    IDLE = 1
    SHIFT = 2
    ATTACK = 3
    score = 0

    def __init__(self, name):
        self.name = name
        self.position = pygame.Vector2(640, 360)
        self.radius = 50
        self.timer = 0
        self.set_idle()

    def set_idle(self):
        self.timer = random.randint(2, 8)
        self.state = self.IDLE
        self.score += 1
        
    def set_shift(self):
        self.timer = random.randint(2, 8)
        self.state = self.SHIFT
    
    def set_attack(self):
        self.timer = random.randint(2, 8)
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

