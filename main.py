import pygame
from player import Player
from boss import Boss

'''
Current State	Event	                    Next State	           
RUNNING (1)	    P key pressed	            PAUSED (2)	
RUNNING (1)	    Game over condition met	    GAME_OVER (3)	
RUNNING (1)	    No event	                RUNNING (1)	
PAUSED (2)	    P key pressed	            RUNNING (1)
PAUSED (2)	    Quit event	                PAUSED (2)	
PAUSED (2)	    No event	                PAUSED (2)	
GAME_OVER (3)	Q key pressed	            Quit	
GAME_OVER (3)	No event	                GAME_OVER (3)
'''

# INITIALIZE PYGAME
pygame.init()

# CREATE SCREEN
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
# TITLE AND ICON
pygame.display.set_caption("AUTOMATA PROJECT")
icon = pygame.image.load('pikachu.png')
pygame.display.set_icon(icon)

pygame.font.init()
font = pygame.font.Font(None, 36)

dt = 0

score = 0

player = Player((screen.get_width() / 2, screen.get_height() / 2))
boss = Boss("2.9")

# Game states
RUNNING = 1
PAUSED = 2
GAME_OVER = 3

game_state = RUNNING

def check_stat(player_state, boss_state):
    if player_state != Player.IDLE and boss_state == Boss.SHIFT:
        return GAME_OVER
    elif player_state == Player.WALK and boss_state == Boss.ATTACK:
        return GAME_OVER
    return RUNNING

def draw_text(text, position, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

# GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if game_state == RUNNING:
                    game_state = PAUSED
                elif game_state == PAUSED:
                    game_state = RUNNING

    if game_state == RUNNING:
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        player.handle_input(keys, mouse)
        player.update(dt)
        boss.update(dt)

        game_state = check_stat(player.state, boss.state)

        screen.fill((0, 202, 255))
        player.draw(screen)
        boss.draw(screen)

        player_state_text = f"Player State: {player.state}"
        boss_state_text = f"Boss State: {boss.state}"
        score_text = f"Score: {boss.score}"
        draw_text(score_text, (10, 10))
        draw_text(player_state_text, (10, 50))
        draw_text(boss_state_text, (10, 100))
    
    elif game_state == PAUSED:
        screen.fill((0, 0, 0))
        draw_text("Game Paused", (540, 360), color=(255, 255, 255))

    elif game_state == GAME_OVER:
        screen.fill((0, 0, 0))
        draw_text("Game Over", (540, 360), color=(255, 0, 0))
        draw_text("Press Q to Quit", (540, 400), color=(255, 255, 255))

    pygame.display.flip()

    if game_state == GAME_OVER:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            running = False

    dt = clock.tick(60) / 1000

pygame.quit()
