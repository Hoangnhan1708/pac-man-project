import heapq
import random
import numpy as np
import extract
import render
from pygame import event, QUIT, display, time
from collections import deque

previous_direction = None

# Get Pacman vision range 3x3
def pacman_visibility_range(matrix, pacman_position):
    pacman_vision_matrix = np.zeros((30, 30))
    range =  [0 , 1, -1, 2 , -2, 3, -3]
    
    for i in range:
        for j in range:
            if 0 <= pacman_position[0] + i < len(pacman_vision_matrix) and 0 <= pacman_position[1] + j < len(pacman_vision_matrix):
                pacman_vision_matrix[pacman_position[0] + i, pacman_position[1] + j] = matrix[pacman_position[0] + i, pacman_position[1] + j]
            else:
                break

    return pacman_vision_matrix


def save_previous_direction(start):
    previous_direction = start
    return previous_direction

def go_random(matrix, start):
    valid_paths = []
    global previous_direction
    # Lấy danh sách các hướng có thể đi
    for neighbor in get_neighbors(matrix,start):
         valid_paths.append(neighbor)

    # Lọc bỏ hướng trước đó khỏi danh sách hướng có thể đi
    if previous_direction in valid_paths:
        if(len(valid_paths) != 1):
            valid_paths.remove(previous_direction)
            
    # Nếu còn ít nhất một hướng có thể đi, chọn một hướng ngẫu nhiên
    if valid_paths:
        next_random_step_index = random.sample((range(0, len(valid_paths))), k=1)
        previous_direction = start
        return valid_paths[next_random_step_index[0]]
    else:
        return start

    
# Heuristic function (h(x): estimated distance from processing location to goal)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Get neighbors of a given point
def get_neighbors(matrix, node): # node = tuple (x,y) => node[0] = x, node[1] = y
    neighbors = []
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # Phải trái trên dưới
        if 0 <= node[0] + i < len(matrix) and 0 <= node[1] + j < len(matrix[0]) and matrix[node[0] + i][node[1] + j] != 1 : # check index of node is out of range and not a wall
            if 0 <= node[0] + i < len(matrix) and 0 <= node[1] + j < len(matrix[0]) and matrix[node[0] + i][node[1] + j] != 3: # treat monster like wall
                neighbors.append((node[0] + i, node[1] + j))   
    return neighbors # tuple (x,y)

def get_neighbors_monster(matrix, node): # this function like above but not process monster
    neighbors = []
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # Phải trái trên dưới
        if 0 <= node[0] + i < len(matrix) and 0 <= node[1] + j < len(matrix[0]) and matrix[node[0] + i][node[1] + j] != 1 : # check index of node is out of range and not a wall
                neighbors.append((node[0] + i, node[1] + j))   
    return neighbors


# A* algorithm
def astar(matrix, start, goal): # start, goal = tuple(x,y)
    open_set = [] # list use to store traveled location
    heapq.heappush(open_set, (0, start))
    came_from = {start: None} # dictionary store {location : its own parent}
    g_score = {start: 0} # g(x) : distance from start location to processing location
    while open_set:
        current = heapq.heappop(open_set)[1] 
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        for neighbor in get_neighbors(matrix, current): 
            temp_g = g_score[current] + 1
            if neighbor not in g_score or temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score = temp_g + heuristic(neighbor, goal) # f(x) = g(x) + h(x)
                heapq.heappush(open_set, (f_score, neighbor))
    return None

def astar_monster(matrix, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {start: None}
    g_score = {start: 0}
    while open_set:
        current = heapq.heappop(open_set)[1] 
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        for neighbor in get_neighbors_monster(matrix, current):
            temp_g = g_score[current] + 1
            if neighbor not in g_score or temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score = temp_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
    
    return None


def find_path_to_food(matrix, pacman_position):
    food_position = None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                food_position = (i,j)        
    if food_position is None:
        return None

    return astar(matrix, pacman_position, food_position)


# Update Pacman's position based on the path found by A*
def update_pacman_position(matrix, pacman_position):
    
    path_to_food = find_path_to_food(matrix, pacman_position)
    
    monster_positions = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 3:
                monster_positions.append((i,j))
    if path_to_food:
        
        next_position = path_to_food[1]  # Lấy vị trí thứ hai trong danh sách đường đi
        if (next_position[0], next_position[1]) in monster_positions:  # Kiểm tra nếu Pacman chạm vào quái vật
            # Kết thúc trò chơi ở đây
            print("Game Over")
            return (-1,-1)
        else:
            matrix[pacman_position[0]][pacman_position[1]] = 999  # Đánh dấu lại vị trí mà Pacman đã đi qua
            matrix[next_position[0]][next_position[1]] = 888  # Di chuyển Pacman đến vị trí tiếp theo

            return next_position
    else:
        # In case of there is no possible path for pacman to eat food, so we just make pacman collide to end the game
        next_position = go_random(matrix, pacman_position)
        
        matrix[pacman_position[0]][pacman_position[1]] = 999  # Đánh dấu lại vị trí mà Pacman đã đi qua
        if (next_position[0], next_position[1]) in monster_positions:
            print("Game Over")
            return (-1,-1)
        matrix[next_position[0]][next_position[1]] = 888  # Di chuyển Pacman đến vị trí tiếp theo

        return next_position



def update_monster_position(matrix, monster_postion):
    # path_to_food = find_path_to_food(matrix, monster_postion, isPacmanFood=True)
    food_position = None
    monsters_default_position = []
    valid_paths = []
    matrix_default = extract.extractMatrix('map3.txt')
    for i in range(len(matrix_default)):
        for j in range(len(matrix_default[0])):
            if matrix_default[i][j] == 3:
                monsters_default_position.append((i,j))
            if matrix[i][j] == 888:
                food_position = (i, j)
    
    
    if monster_postion not in monsters_default_position:
        for position in monsters_default_position:
            if (abs(position[0] - monster_postion[0]) == 1 and (position[1] == monster_postion[1])) or (abs(position[1] - monster_postion[1]) and (position[0] == monster_postion[0])) ==1:
                next_position = position
                break
    else:
        for neighbor in get_neighbors_monster(matrix,monster_postion):
            valid_paths.append(neighbor)
        next_random_step_index =  random.sample((range(0, len(valid_paths))), k=1)
        next_position = valid_paths[next_random_step_index[0]]
    

    # Delete the current postion of ghost
    # Update the next postion
    if (next_position[0], next_position[1]) == food_position:
        print("Game Over")
        return False
    matrix[monster_postion[0]][monster_postion[1]] = 0
    matrix[next_position[0]][next_position[1]] = 3
    return next_position

def update_monsters_postion (matrix):
    monsters_position = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 3:
                monsters_position.append((i,j))
    for monster_position in monsters_position:
        if update_monster_position(matrix, monster_position) == False:
            return False
        
def play(timer, screen):
    fps = 10
    run = True      
    matrix = extract.extractMatrix('map{}.txt'.format(3))
    player_location = extract.extractLocation('map{}.txt'.format(3))      
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
        matrix[player_x][player_y] = 999
        matrix_visible_range = pacman_visibility_range(matrix, (player_x,player_y))
        (player_x, player_y) = update_pacman_position(matrix_visible_range, (player_x, player_y))
        if update_monsters_postion(matrix_visible_range) == False:
            run = False
        
        if (player_x, player_y) == (-1,-1):
            run =False
        score_value -= 1
        if score_value == 0:
            run = False
        if matrix[player_x][player_y] == 2:
            score_value += 20

        render.render(matrix_visible_range)
        render.render_score(300,700, score_value)
        for eventElement in event.get():
            if eventElement.type == QUIT:
                run = False
        display.flip()
