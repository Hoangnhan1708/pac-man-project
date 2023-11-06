# #Các cơ chế game sẽ được lưu trong đây
# import resources as r
# def rungame(levelGame):
#     run = True
#     if  levelGame == 'Level1':
#         r.resourcesSetup('map1.txt')
#     elif levelGame == 'Level2':
#         r.resourcesSetup(r.map2)
#     while run:      
#         r.timer.tick(r.fps)
#         if r.counter < 19:
#             r.counter+=1
#         else:
#             r.counter = 0         
#         r.screen.fill('black')      
#         if levelGame == 'Level1':
#             if r.gameplay1.update_pacman_position(r.matrix, (r.player_x, r.player_y)):
#                 r.player_x, r.player_y = r.gameplay1.update_pacman_position(r.matrix, (r.player_x, r.player_y))
#                 r.score_value -= 1
#                 if r.score_value == 0:
#                     run = False
#             else:
#                 run = False

#         r.render.render(r.matrix)
#         r.render.render_core(300,700)
#         r.pygame.display.flip()
#         for event in r.pygame.event.get():
#             if event.type == r.pygame.QUIT:
#                 run = False      
#     r.pygame.quit()


# def game_play():
    
#     while True:
#         for event in r.pygame.event.get():
#             if event.type == r.pygame.QUIT:
#                 r.pygame.quit()
#                 quit()

#         r.screen.fill((0,0,0)) # Black color for screen
#         largeText = r.pygame.font.Font('source/assets/font/freesansbold.ttf', 100)#Tạo phông chữ với kích cỡ 100 pixel
#         TextSurf, TextRect = r.render.text_objects("Pacman Game", largeText)
#         TextRect.center = ((r.WIDTH / 2), (45))
#         r.screen.blit(TextSurf, TextRect)

#         # Creating buttons
#         mouse = r.pygame.mouse.get_pos()
#         click = r.pygame.mouse.get_pressed()

#         # Start button
#         if 290 < mouse[0] < 410 and 120 <mouse[1] <180:#Nếu di chuyển chuột vào vugnf này
#             r.pygame.draw.rect(r.screen, (0,200,0), (290,120,120,60)) # Brighter when hover
#             if click[0] == 1:               
#                 r.pygame.mouse.set_pos((289,119))
#                 r.render.renderlevelgame()#Chạy chương trình
#         else:
#             r.pygame.draw.rect(r.screen, (0,255,0), (290,120,120,60)) # Darker normally

#         smallText = r.pygame.font.Font("source/assets/font/freesansbold.ttf", 20)
#         TextSurf, TextRect = r.render.text_objects("Start Game", smallText)
#         TextRect.center = ((350), (150))#Vị trí chữ
#         r.screen.blit(TextSurf, TextRect)
         
#         # Credit Button
#         if 290 < mouse[0] < 410 and 200 <mouse[1] <260:#Nếu di chuyển chuột vào vugnf này
#             r.pygame.draw.rect(r.screen, (255,250,0), (290,200,120,60)) # Brighter when hover
#             if click[0] == 1:
#                 print("No thing")#Chạy chương trình
#         else:
#             r.pygame.draw.rect(r.screen, (255,150,0), (290,200,120,60)) # Darker normally
    
#         smallText = r.pygame.font.Font("source/assets/font/freesansbold.ttf", 20)
#         TextSurf, TextRect = r.render.text_objects("Credit", smallText)
#         TextRect.center = ((350), (230))#Vị trí chữ
#         r.screen.blit(TextSurf, TextRect)
        
             
#         # Quit button
#         if 290 < mouse[0] < 410  and 280 <mouse[1] <340:
#             r.pygame.draw.rect(r.screen, (200,0,0), (290,280,120,60)) # Brighter when hover
#             if click[0] == 1:
#                 r.pygame.quit()
#                 quit()
#         else:
#             r.pygame.draw.rect(r.screen, (255,0,0), (290,280,120,60)) # Darker normally

#         smallText = r.pygame.font.Font("source/assets/font/freesansbold.ttf", 19)
#         TextSurf, TextRect = r.render.text_objects("Quit Game", smallText)
#         TextRect.center = (350,310)
#         r.screen.blit(TextSurf, TextRect)
#         r.pygame.display.flip()

