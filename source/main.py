import pygame
import numpy as np
import extract
import gameplay1 
import gameplay2 
import gameplay3
import random


pygame.init()
pygame.font.init()
WIDTH = 700 # width of console
HEIGHT = 750 # height of console
screen = pygame.display.set_mode([WIDTH,HEIGHT])
timer = pygame.time.Clock()
fps = 10
font = pygame.font.Font('source/assets/font/freesansbold.ttf',32)
color_wall = 'blue'
color_monster = 'white'
color_food = 'red'

# matrix = extract.extractMatrix('map1.txt')
matrix = extract.extractMatrix('map3.txt')

rows, cols = len(matrix), len(matrix[0])
width_tile = (WIDTH//cols) # width of each piece
height_tile = ((HEIGHT - 50) //rows) # height of each piece

player_location = extract.extractLocation('map3.txt')
player_x = player_location[0] 
player_y = player_location[1]

matrix[player_x][player_y] = 4
direction = 0
counter = 0

score_value = 10000000000


# Get image 
player_images=[]
for i in range(1,5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'source/assets/player_images/{i}.png'),(20,20)))

monster_image =pygame.transform.scale(pygame.image.load(f'source/assets/monster_images/blue.png'),(20,20))

food_image = pygame.transform.scale(pygame.image.load(f'source/assets/food_image/apple.png'),(25,25))

def render_core(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))


def render(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1: # Wall
                pygame.draw.rect(screen, color_wall, pygame.Rect(j* width_tile + (0.3 * width_tile) , i * height_tile + (0.3 * height_tile) , width_tile, height_tile))
                
            if matrix[i][j] == 2: # Food
                screen.blit(food_image, (j* width_tile + (0.3 * width_tile), i* height_tile + (0.3 * height_tile)))
                
            
            if matrix[i][j] == 3: # Monster
                screen.blit(monster_image, (j* width_tile + (0.3 * width_tile), i* height_tile + (0.3 * height_tile)))
            
            if matrix[i][j] == 4: # Pacman
                screen.blit(player_images[counter // 5], (j* width_tile + (0.3 * width_tile), i* height_tile + (0.3 * height_tile)))
            
            if matrix[i][j] == 5: # Location which pacman gone
                pygame.draw.circle(screen, 'white', (j* width_tile + (0.7 * width_tile)  , i * height_tile + (0.7 * height_tile) ) , 5)


run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter+=1
    else:
        counter = 0
    screen.fill('black')
    matrix[player_x][player_y] = 5
    matrix_visible_range = gameplay3.pacman_visibility_range(matrix, (player_x,player_y))
    # matrix_visible_range = gameplay3.move_pacman(matrix,(player_x,player_y))
    # player_x, player_y = gameplay1.update_pacman_position(matrix, (player_x, player_y))
    #player_x, player_y = gameplay2.update_pacman_position(matrix, (player_x, player_y))
    gameplay3.update_monsters_postion(matrix_visible_range)
    (player_x, player_y) = gameplay3.update_pacman_position(matrix_visible_range, (player_x, player_y))
    
    if (player_x, player_y) == (-1,-1):
        run =False
    score_value -= 1
    if score_value == 0:
        run = False
    
    render(matrix_visible_range)
    render_core(300,700)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.flip()
pygame.quit()