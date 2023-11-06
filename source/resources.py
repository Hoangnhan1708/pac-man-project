# #Nơi lưu trữ các tài nguyên của chương trình
# import pygame   
# import heapq
# import math
# import numpy as np
# import logic
# import gameplay2
# import gameplay1
# import render
# import gamemechanics 
# pygame.init()
# pygame.font.init()
# WIDTH = 700 # width of console
# HEIGHT = 750 # height of console
# screen = pygame.display.set_mode([WIDTH,HEIGHT])
# timer = pygame.time.Clock()
# fps = 10
# font = pygame.font.Font('source/assets/font/freesansbold.ttf',32)
# color_wall = 'blue'
# color_monster = 'white'
# color_food = 'red'
# map1='map1.txt'
# map2='map2.txt'
# map3='map3.txt'
# map4='map4.txt'
# map5='map5.txt'
# matrixTemp=np.zeros((int(50),int(50)))
# player_locationTemp=(int(0),int(0))
# def resourcesSetup(map):
   
# matrix = matrixTemp.copy()
# player_location = player_locationTemp
# rows, cols = len(matrix), len(matrix[0])
# width_tile = (WIDTH//cols) # width of each piece
# height_tile = ((HEIGHT - 50) //rows) # height of each piece

# #player_location = logic.extractLocation('map1.txt')
# player_x = player_location[0] 
# player_y = player_location[1]

# matrix[player_x][player_y] = 4
# direction = 0
# counter = 0

# score_value = 100

# monster_image =pygame.transform.scale(pygame.image.load(f'source/assets/monster_images/blue.png'),(20,20))

# food_image = pygame.transform.scale(pygame.image.load(f'source/assets/food_image/apple.png'),(25,25))
