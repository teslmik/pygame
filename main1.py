import pygame
import random

pygame.init()

HEIGHT = 800
WIDTH = 1200
COLOR_WHITE = (255, 255, 255)
COLOR_BlACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
surf = pygame.Surface((150, 150))
playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
main_display.blit(player, player_rect)

pygame.display.flip()

player_speed = [1, 1]
player_rect = player_rect.move(player_speed)
main_display.fill(COLOR_BlACK)

FPS = pygame.time.Clock()
FPS.tick(120)

if player_rect.bottom >= HEIGHT:
    player_speed = random.choice(([1, -1], [-1, -1]))
if player_rect.right >= WIDTH:
    player_speed = random.choice(([-1, 1], [1, 1]))

keys = pygame.key.get_pressed()

from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

if keys[K_LEFT]:
    print('Натиснута клавіша вліво')

player_move_down = [0, 1]

if keys[K_DOWN] and player_rect.bottom < HEIGHT:
    player_rect = player_rect.move(player_move_down)

def create_enemy():

    enemy_size = (30, 30)
    enemy = pygame.Surface(enemy_size)
    enemy.fill(COLOR_BLUE)
    enemy_rect = pygame.Rect(WIDTH, 100, *enemy_size)
    enemy_move = [-1, 0]

    return [enemy, enemy_rect, enemy_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

enemies = []
for event in pygame.event.get():
    if event.type == QUIT:
        playing = False
    if event.type == CREATE_ENEMY:
        enemies.append(create_enemy())