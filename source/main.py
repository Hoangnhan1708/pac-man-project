import pygame
import logic
pygame.init()
import numpy as np
WIDTH = 900 # width of console
HEIGHT = 950 # height of console
screen = pygame.display.set_mode([WIDTH,HEIGHT])
timer = pygame.time.Clock()
fps = 60
colorWall = 'blue'
colorMonster = 'white'
colorFood = 'red'
playerImages=[]
level = logic.extractMatrix('map1.txt')

rows, cols = len(level), len(level[0])
widthTile = (WIDTH//cols) # width of each piece
heightTile = ((HEIGHT - 50) //rows) # height of each piece

playerLocation = logic.extractLocation('map1.txt')
playerX = playerLocation[0] 
playerY = playerLocation[1] 
level[playerX][playerY] = 4
direction = 0
counter = 0

#Get image of Pacman
for i in range(1,5):
    playerImages.append(pygame.transform.scale(pygame.image.load(f'source/assets/player_images/{i}.png'),(20,20)))

monsterImage =pygame.transform.scale(pygame.image.load(f'source/assets/monster_images/blue.png'),(20,20))

def drawBoard(level):
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.rect(screen, colorWall, pygame.Rect(j* widthTile  , i * heightTile , widthTile, heightTile),10)
                
            if level[i][j] == 2:
                pygame.draw.circle(screen,colorFood, (j* widthTile , i * heightTile ) , 10 )
            
            if level[i][j] == 3:
                screen.blit(monsterImage, (j* widthTile + (0.3 * widthTile), i* heightTile + (0.3 * heightTile)))
            
            if level[i][j] == 4:
                screen.blit(playerImages[counter // 5], (j* widthTile + (0.3 * widthTile), i* heightTile + (0.3 * heightTile)))

 

run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter+=1
    else:
        counter = 0
    screen.fill('black')
    drawBoard(level)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
            
    pygame.display.flip()
pygame.quit()




