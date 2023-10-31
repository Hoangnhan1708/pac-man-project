import pygame
import logic
pygame.init()
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
playerX = playerLocation[0] * widthTile + (0.3 * widthTile)
playerY = playerLocation[1] * heightTile + (0.3 * heightTile)
direction = 0
counter = 0

#Get image of Pacman
for i in range(1,5):
    playerImages.append(pygame.transform.scale(pygame.image.load(f'source/assets/player_images/{i}.png'),(20,20)))

def drawBoard(level):
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.rect(screen, colorWall, pygame.Rect(j* widthTile  , i * heightTile , widthTile, heightTile),10)
                
            if level[i][j] == 2:
                pygame.draw.circle(screen,colorFood, (j* widthTile , i * heightTile ) , 10 )
            
            if level[i][j] == 3:
                pygame.draw.circle(screen,colorMonster, (j* widthTile , i * heightTile ) , 10 )



def drawPlayer():
    # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
    if direction == 0:
        screen.blit(playerImages[counter // 5], (playerX,playerY))
    elif direction == 1:
        screen.blit(pygame.transform.flip(playerImages[counter // 5], True, False), (playerX,playerY))
    elif direction == 2:
        screen.blit(pygame.transform.rotate(playerImages[counter // 5], 90), (playerX,playerY))
    elif direction == 3:
        screen.blit(pygame.transform.rotate(playerImages[counter // 5],270), (playerX,playerY))



run = True
while run:
    timer.tick(fps)
    if counter < 19:
        counter+=1
    else:
        counter = 0
    screen.fill('black')
    drawBoard(level)
    drawPlayer()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 0
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_UP:
                direction = 2
            if event.key == pygame.K_DOWN:
                direction = 3
            
    pygame.display.flip()
pygame.quit()



