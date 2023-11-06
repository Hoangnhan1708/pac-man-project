import render
import pygame   
import heapq
import math
import numpy as np
import logic
import gameplay2
import gameplay1
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

monster_image =pygame.transform.scale(pygame.image.load(f'source/assets/monster_images/blue.png'),(20,20))
food_image = pygame.transform.scale(pygame.image.load(f'source/assets/food_image/apple.png'),(25,25))
return_image =pygame.transform.scale(pygame.image.load(f'source/assets/return_images/return_images.png'),(30,30))

creditFont = pygame.font.Font("source/assets/font/freesansbold.ttf", 20)
creditList = [
    "21120402 - Truong Hoang Nhan",
    "21120403 - Nguyen Hoang Quan",
    "21120406 - Le Viet Dat Trong",
    "21120416 - Ha Quoc Bao"
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((0,0,0)) # Black color for screen
    largeText = pygame.font.Font('source/assets/font/freesansbold.ttf', 100)#Tạo phông chữ với kích cỡ 100 pixel
    TextSurf, TextRect = render.text_objects("Pacman Game", largeText)
    TextRect.center = ((WIDTH / 2), (45))
    screen.blit(TextSurf, TextRect)

    # Creating buttons
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    

    # Start button
    if 290 < mouse[0] < 410 and 120 <mouse[1] <180:#Nếu di chuyển chuột vào vugnf này       
        pygame.draw.rect(screen, (0,200,0), (290,120,120,60)) # Brighter when hover
        if click[0] == 1:               
            pygame.mouse.set_pos((289,119))
            run_Level=True
            while run_Level:        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.fill((0,0,0)) # Black color for screen

                # Creating buttons
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                # Level 1
                if 290 < mouse[0] < 410 and 120 <mouse[1] <180:#Nếu di chuyển chuột vào vugnf này
                    pygame.draw.rect(screen, (0,200,0), (290,120,120,60)) # Brighter when hover
                    if click[0] == 1:
                        run = True        
                        matrix = logic.extractMatrix('map1.txt')
                        player_location = logic.extractLocation('map1.txt')      
                        direction = 0
                        counter = 0
                        score_value = 100           
                        player_x = player_location[0] 
                        player_y = player_location[1]
                        while run:      
                            timer.tick(fps)
                            if counter < 19:
                                counter+=1
                            else:
                                counter = 0                                        
                            screen.fill('black')                                      
                            if gameplay1.update_pacman_position(matrix, (player_x, player_y)):
                                player_x, player_y = gameplay1.update_pacman_position(matrix, (player_x, player_y))
                                score_value -= 1
                                if score_value == 0:
                                    run = False
                            else:
                                run = False

                            render.render(matrix)
                            render.render_core(300,700,score_value)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        run = False   
                            pygame.display.flip()     
                                                                             
                else:
                    pygame.draw.rect(screen, (0,255,0), (290,120,120,60)) # Darker normally
                    
                smallText = pygame.font.Font("source/assets/font/freesansbold.ttf", 20)
                TextSurf, TextRect = render.text_objects("Level 1", smallText)
                TextRect.center = ((350), (150))#Vị trí chữ
                screen.blit(TextSurf, TextRect)
                                        
                # Level 2
                if 290 < mouse[0] < 410 and 200 <mouse[1] <260:#Nếu di chuyển chuột vào vùng này
                    pygame.draw.rect(screen, (255,250,0), (290,200,120,60)) # Brighter when hover
                    if click[0] == 1:
                        run = True        
                        matrix = logic.extractMatrix('map2.txt')
                        player_location = logic.extractLocation('map2.txt')      
                        direction = 0
                        counter = 0
                        score_value = 100            
                        player_x = player_location[0] 
                        player_y = player_location[1]
                        while run:      
                            timer.tick(fps)
                            if counter < 19:
                                counter+=1
                            else:
                                counter = 0                                        
                            screen.fill('black')                                      
                            if gameplay2.update_pacman_position(matrix, (player_x, player_y)):
                                player_x, player_y = gameplay2.update_pacman_position(matrix, (player_x, player_y))
                                score_value -= 1
                                if score_value == 0:
                                    run = False
                            else:
                                run = False

                            render.render(matrix)
                            render.render_core(300,700,score_value)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        run = False   
                            pygame.display.flip()     
                                             
                else:
                    pygame.draw.rect(screen, (255,150,0), (290,200,120,60)) # Darker normally
            
                smallText = pygame.font.Font("source/assets/font/freesansbold.ttf", 20)
                TextSurf, TextRect = render.text_objects("Level 2", smallText)
                TextRect.center = ((350), (230))#Vị trí chữ
                screen.blit(TextSurf, TextRect)
                            
                # Level 3
                if 290 < mouse[0] < 410  and 280 <mouse[1] <340:
                    pygame.draw.rect(screen, (200,0,0), (290,280,120,60)) # Brighter when hover
                    if click[0] == 1:
                        print("oke")#Run Level 3
                        
                else:
                    pygame.draw.rect(screen, (255,0,0), (290,280,120,60)) # Darker normally

                smallText = pygame.font.Font("source/assets/font/freesansbold.ttf", 19)
                TextSurf, TextRect = render.text_objects("Level 3", smallText)
                TextRect.center = (350,310)
                screen.blit(TextSurf, TextRect)                
                
                # Level 4
                if 290 < mouse[0] < 410  and 360 <mouse[1] <420:
                    pygame.draw.rect(screen, (128, 0, 128), (290,360,120,60)) # Brighter when hover
                    if click[0] == 1:
                        print("oke")#Run Level 4
                        
                else:
                    pygame.draw.rect(screen, (139, 0, 139), (290,360,120,60)) # Darker normally

                smallText = pygame.font.Font("source/assets/font/freesansbold.ttf", 19)
                TextSurf, TextRect = render.text_objects("Level 4", smallText)
                TextRect.center = (350,390)
                screen.blit(TextSurf, TextRect)
                
                
                if 30 < mouse[0] < 60  and 30 <mouse[1] <60:
                    screen.blit(return_image, (30, 30)) 
                    pygame.draw.rect(screen, (255,255,255), (30,30,30,30)) # Brighter when hover
                    if click[0] == 1:
                        run_Level=False                       
                else:
                    pygame.draw.rect(screen, (50, 50, 50), (30,30,30,30)) # Darker normally                    
                screen.blit(return_image, (30, 30))    
                pygame.display.flip()
    else:
        pygame.draw.rect(screen, (0,255,0), (290,120,120,60))   
                                                                                        
    smallText = pygame.font.Font("source/assets/font/freesansbold.ttf", 20)
    TextSurf, TextRect = render.text_objects("Start Game", smallText)
    TextRect.center = ((350), (150))#Vị trí chữ
    screen.blit(TextSurf, TextRect)
        
    # Credit Button
    if 290 < mouse[0] < 410 and 200 <mouse[1] <260:#Nếu di chuyển chuột vào vugnf này
        pygame.draw.rect(screen, (255,250,0), (290,200,120,60)) # Brighter when hover
        if click[0] == 1:
            show_Credit=True
            while show_Credit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                screen.fill((0,0,0)) # Black color for screen
                for i, line in enumerate(creditList):
                    lineSurface, lineRect = render.text_objects(line, creditFont)
                    lineRect.center = (WIDTH / 2, 200 + 30*i) # Adjust as necessary
                    screen.blit(lineSurface, lineRect)
                mouse = pygame.mouse.get_pos()    # Update mouse position
                click = pygame.mouse.get_pressed()  # Update mouse clicks
                if 30 < mouse[0] < 60  and 30 <mouse[1] <60:
                    screen.blit(return_image, (30, 30)) 
                    pygame.draw.rect(screen, (255,255,255), (30,30,30,30)) # Brighter when hover
                    if click[0] == 1:
                        show_Credit=False                       
                else:
                    pygame.draw.rect(screen, (50, 50, 50), (30,30,30,30)) # Darker normally                    
                screen.blit(return_image, (30, 30))    
                pygame.display.update()
    else:
        pygame.draw.rect(screen, (255,150,0), (290,200,120,60)) # Darker normally

    smallText = pygame.font.Font("source/assets/font/freesansbold.ttf", 20)
    TextSurf, TextRect = render.text_objects("Credit", smallText)
    TextRect.center = ((350), (230))#Vị trí chữ
    screen.blit(TextSurf, TextRect)
    
            
    # Quit button
    if 290 < mouse[0] < 410  and 280 <mouse[1] <340:
        pygame.draw.rect(screen, (200,0,0), (290,280,120,60)) # Brighter when hover
        if click[0] == 1:
            pygame.quit()
            quit()
    else:
        pygame.draw.rect(screen, (255,0,0), (290,280,120,60)) # Darker normally

    smallText = pygame.font.Font("source/assets/font/freesansbold.ttf", 19)
    TextSurf, TextRect = render.text_objects("Quit Game", smallText)
    TextRect.center = (350,310)
    screen.blit(TextSurf, TextRect)
    pygame.display.flip()