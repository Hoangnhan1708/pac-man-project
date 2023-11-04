import pygame
import heapq
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
        
        for neighbor in get_neighbors(matrix, current): # Xem ở đây sẽ hiểu : https://www.youtube.com/watch?v=G7XnNtF7UEE&t=368s&ab_channel=%C4%90%E1%BB%97Ph%C3%BAcH%E1%BA%A3o
            temp_g = g_score[current] + 1
            if neighbor not in g_score or temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score = temp_g + heuristic(neighbor, goal) # f(x) = g(x) + h(x)
                heapq.heappush(open_set, (f_score, neighbor))
    return None

# A* algorithm with existence of ghost in no mind.
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

# Find nearest available food


def find_path_to_food(matrix, pacman_position, multipleFood=False, isPacmanFood=False):
    food_position = None
    if is_more_food(matrix):
        if isPacmanFood == False:
            if multipleFood==False:
                for i in range(len(matrix)):
                    for j in range(len(matrix[0])):
                        if matrix[i][j] == 2:
                            food_position = (i,j)
        else:
            for i in range(len(matrix)):
                    for j in range(len(matrix[0])):
                        if matrix[i][j] == 4:
                            food_position = (i,j)
        if food_position is None:
            return None

        return astar(matrix, pacman_position, food_position)
    else:
        return False
        

def is_more_food(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                return True
    return False



# Update Pacman's position based on the path found by A*
def update_pacman_position(matrix, pacman_position):
    if is_more_food(matrix):
        path_to_food = find_path_to_food(matrix, pacman_position )
        food_position = None
        monster_positions = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 2:
                    food_position = (i, j)
                if matrix[i][j] == 3:
                    monster_positions.append((i,j))
        
        if path_to_food:
            next_position = path_to_food[1]  # Lấy vị trí thứ hai trong danh sách đường đi
            if matrix[next_position[0]][next_position[1]] == 3:  # Kiểm tra nếu Pacman chạm vào quái vật
                # Kết thúc trò chơi ở đây
                print("Game Over")
                return False
            else:
                matrix[pacman_position[0]][pacman_position[1]] = 5  # Đánh dấu lại vị trí mà Pacman đã đi qua
                matrix[next_position[0]][next_position[1]] = 4  # Di chuyển Pacman đến vị trí tiếp theo
                if (next_position[0], next_position[1]) == food_position:
                    print("You Win")
                    return False
                return next_position
        else:

            path_to_monster = astar_monster(matrix, pacman_position, food_position) # still the shortest way to food but pacman might collide with monster
            next_position = path_to_monster[1] if path_to_monster else pacman_position

            matrix[pacman_position[0]][pacman_position[1]] = 5  # Đánh dấu lại vị trí mà Pacman đã đi qua
            if (next_position[0], next_position[1]) in monster_positions:
                print("Game Over")
                return False
            matrix[next_position[0]][next_position[1]] = 4  # Di chuyển Pacman đến vị trí tiếp theo
            return next_position
    else:
        return False

def update_monster_position (matrix, monster_postion):
    # path_to_food = find_path_to_food(matrix, monster_postion, isPacmanFood=True)
    food_position = None

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 4:
                food_position = (i, j)

    path_to_monster = astar_monster(matrix, monster_postion, food_position)
    next_position = path_to_monster[1] if path_to_monster else monster_postion

    # Delete the current postion of ghost
    matrix[monster_postion[0]][monster_postion[1]] = 0
    # Update the next postion
    matrix[next_position[0]][next_position[1]] = 3

    if (next_position[0], next_position[1]) == food_position:
        print("Game Over")
        return False
    return next_position


def update_monsters_postion (matrix):
    monsters_position = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 3:
                monsters_position.append((i,j))
    for monster_position in monsters_position:
        update_monster_position(matrix, monster_position)
