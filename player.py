import pygame

'''
Current State	Mouse Click	LCTRL Pressed	Movement Keys Pressed	Next State
IDLE (1)	    Yes	        -	            -	                    IDLE (1)
IDLE (1)	    No	        Yes	            -	                    ATTACK (3)
IDLE (1)	    No	        No	            Yes	                    WALK (2)
IDLE (1)	    No	        No	            No	                    IDLE (1)
WALK (2)	    Yes	        -	            -	                    IDLE (1)
WALK (2)	    No	        Yes	            -	                    ATTACK (3)
WALK (2)	    No	        No	            Yes	                    WALK (2)
WALK (2)	    No	        No	            No	                    IDLE (1)
ATTACK (3)	    Yes	        -	            -	                    IDLE (1)
ATTACK (3)	    No	        Yes	            -	                    ATTACK (3)
ATTACK (3)	    No	        No	            Yes                 	WALK (2)
ATTACK (3)	    No	        No	            No	                    IDLE (1)

'''

class Player:
    IDLE = 1
    WALK = 2
    ATTACK = 3

    def __init__(self, position):
        self.position = pygame.Vector2(position)
        self.speed = 50
        self.state = self.IDLE

    def handle_input(self, keys, mouse):
        moving_keys = [pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_s]

        if mouse[0]:
            self.state = self.IDLE
        elif keys[pygame.K_LCTRL]:
                self.state = self.ATTACK
        elif any(keys[key] for key in moving_keys):
            self.state = self.WALK

    def update(self, dt):
        if self.state == self.WALK:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.position.y -= self.speed * dt
            if keys[pygame.K_s]:
                self.position.y += self.speed * dt
            if keys[pygame.K_a]:
                self.position.x -= self.speed * dt
            if keys[pygame.K_d]:        
                self.position.x += self.speed * dt
    
    def draw(self, screen):

        if self.state == self.IDLE:
            color = "red"
        elif self.state == self.WALK:
            color = "yellow"
        elif self.state == self.ATTACK:
            color = "blue"

        pygame.draw.circle(screen, color, self.position, 10)
