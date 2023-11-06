#Xử lý các tác vụ liên quan đến đồ họa
import pygame
import logic
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
matrix = logic.extractMatrix('map1.txt')

rows, cols = len(matrix), len(matrix[0])
width_tile = (WIDTH//cols) # width of each piece
height_tile = ((HEIGHT - 50) //rows) # height of each piece

direction = 0
counter = 0
score_value = 100
monster_image =pygame.transform.scale(pygame.image.load(f'source/assets/monster_images/blue.png'),(20,20))
food_image = pygame.transform.scale(pygame.image.load(f'source/assets/food_image/apple.png'),(25,25))

# Get image 
player_images=[]
for i in range(1,5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'source/assets/player_images/{i}.png'),(20,20)))


def render_core(x,y,score_value):
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

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255)) # White color for text
    return textSurface, textSurface.get_rect()

         
        

