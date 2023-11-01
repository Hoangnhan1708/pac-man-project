import pygame
import logic
import gameplay1 
import gameplay2 

pygame.init()
pygame.font.init()
import numpy as np
WIDTH = 700 # width of console
HEIGHT = 750 # height of console
screen = pygame.display.set_mode([WIDTH,HEIGHT])
timer = pygame.time.Clock()
fps = 10
colorWall = 'blue'
colorMonster = 'white'
colorFood = 'red'
playerImages=[]
# matrix = logic.extractMatrix('map1.txt')
matrix = logic.extractMatrix('map2.txt')

rows, cols = len(matrix), len(matrix[0])
widthTile = (WIDTH//cols) # width of each piece
heightTile = ((HEIGHT - 50) //rows) # height of each piece

playerLocation = logic.extractLocation('map1.txt')
playerX = playerLocation[0] 
playerY = playerLocation[1] 
matrix[playerX][playerY] = 4
direction = 0
counter = 0

score_value = 0
font = pygame.font.Font('source/assets/font/freesansbold.ttf',32)


# Get image of Pacman
for i in range(1,5):
    playerImages.append(pygame.transform.scale(pygame.image.load(f'source/assets/player_images/{i}.png'),(20,20)))

monsterImage =pygame.transform.scale(pygame.image.load(f'source/assets/monster_images/blue.png'),(20,20))

foodImage = pygame.transform.scale(pygame.image.load(f'source/assets/food_image/apple.png'),(25,25))

def showScore(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))


def render(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                pygame.draw.rect(screen, colorWall, pygame.Rect(j* widthTile + (0.3 * widthTile) , i * heightTile + (0.3 * heightTile) , widthTile, heightTile))
                
            if matrix[i][j] == 2:
                # pygame.draw.circle(screen,colorFood, (j* widthTile + (0.3 * widthTile), i * heightTile + (0.3 * heightTile)) ,5)
                screen.blit(foodImage, (j* widthTile + (0.3 * widthTile), i* heightTile + (0.3 * heightTile)))
                
            
            if matrix[i][j] == 3:
                screen.blit(monsterImage, (j* widthTile + (0.3 * widthTile), i* heightTile + (0.3 * heightTile)))
            
            if matrix[i][j] == 4:
                screen.blit(playerImages[counter // 5], (j* widthTile + (0.3 * widthTile), i* heightTile + (0.3 * heightTile)))



run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter+=1
    else:
        counter = 0
    screen.fill('black')
    playerX, playerY = gameplay2.update_pacman_position(matrix, (playerX, playerY))
    # playerX, playerY = gameplay1.update_pacman_position(matrix, (playerX, playerY))
    matrix[playerX][playerY] = 4
    render(matrix)
    showScore(300,700)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.flip()
pygame.quit()





