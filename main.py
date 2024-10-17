import pygame
from player import Player
from boss import Boss
# INITITALIZE PYGAME
pygame.init()

# CREATE SCREEN
screen = pygame.display.set_mode( (1280, 720) )
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

def check_stat(player_state, boss_state):
    if player_state != Player.IDLE and boss_state == Boss.SHIFT:
        print("Game Over")
        pygame.quit()
        exit()
    elif player_state == Player.WALK and boss_state == Boss.ATTACK:
        print("Game Over")
        pygame.quit()
        exit()

def draw_text(text, position, color=(255, 255, 255)):

    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

# GAME LOOP
running = True
while running:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    player.handle_input(keys, mouse)
    player.update(dt)
    boss.update(dt)

    check_stat(player.state, boss.state)

    screen.fill( (0, 202, 255) )
    player.draw(screen)
    boss.draw(screen)

    player_state_text = f"Player State: {player.state}"
    boss_state_text = f"Boss State: {boss.state}"
    score_text = f"Score: {boss.score}" 
    draw_text(score_text, (10, 10))
    draw_text(player_state_text, (10, 50))
    draw_text(boss_state_text, (10, 100))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
