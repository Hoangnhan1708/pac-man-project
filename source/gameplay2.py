import pygame
import heapq
# Heuristic function (h(x): estimated distance from processing location to goal)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Get neighbors of a given point
def get_neighbors(matrix, node):
    neighbors = []
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # Phải trái trên dưới
        if 0 <= node[0] + i < len(matrix) and 0 <= node[1] + j < len(matrix[0]) and matrix[node[0] + i][node[1] + j] != 1 : 
            if 0 <= node[0] + i < len(matrix) and 0 <= node[1] + j < len(matrix[0]) and matrix[node[0] + i][node[1] + j] != 3:
                neighbors.append((node[0] + i, node[1] + j))   
    return neighbors

def get_neighbors_monster(matrix, node):
    neighbors = []
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # Phải trái trên dưới
        if 0 <= node[0] + i < len(matrix) and 0 <= node[1] + j < len(matrix[0]) and matrix[node[0] + i][node[1] + j] != 1 : 
                neighbors.append((node[0] + i, node[1] + j))   
    return neighbors


# A* algorithm
def astar(matrix, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {start: None}
    g_score = {start: 0}
    pathAlter = []
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
                f_score = temp_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
    return None

def astar2monster(matrix, start, goal):
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
    foodPosition = None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                foodPosition = (i,j)        
    if foodPosition is None:
        return None

    return astar(matrix, pacman_position, foodPosition)

def find_path_to_nearest_monster(matrix, pacman_position):
    monster_positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                monster_positions.append((i, j))
    if not monster_positions:
        return None


    nearest_monster = None
    for monster in monster_positions:
        path = astar2monster(matrix, pacman_position, monster)
        print(path)
        if path is not None:
            nearest_monster = monster
            break

            
    if nearest_monster is None:
        return None

    return astar2monster(matrix, pacman_position, nearest_monster)





# Update Pacman's position based on the path found by A*
def update_pacman_position(matrix, pacman_position):
    path_to_food = find_path_to_food(matrix, pacman_position)
    food_position = None
    monster_position = None

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                food_position = (i, j)
            if matrix[i][j] == 3:
                monster_position = (i, j)

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
        # Di chuyển Pacman đến vị trí của quái vật
        path_to_monster = find_path_to_nearest_monster(matrix,monster_position)
        next_position = path_to_monster[1] if path_to_monster else pacman_position

        matrix[pacman_position[0]][pacman_position[1]] = 5  # Đánh dấu lại vị trí mà Pacman đã đi qua
        matrix[next_position[0]][next_position[1]] = 4  # Di chuyển Pacman đến vị trí tiếp theo

        if (next_position[0], next_position[1]) == monster_position:
            print("Game Over")
            return False
        return next_position
    
