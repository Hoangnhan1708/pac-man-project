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


# A* algorithm
def astar(matrix, start, goal):
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
        
        for neighbor in get_neighbors(matrix, current):
            temp_g = g_score[current] + 1
            if neighbor not in g_score or temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score = temp_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))               
    return None

def find_path_to_nearest_food(matrix, pacman_position):
    food_positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                food_positions.append((i, j))
    if not food_positions:
        return None

    valid_food_positions = [pos for pos in food_positions if matrix[pos[0]][pos[1]] != 3]
    if not valid_food_positions:
        return None

    nearest_food = None
    for food in valid_food_positions:
        path = astar(matrix, pacman_position, food)
        if path is not None:
            has_monster = any(matrix[pos[0]][pos[1]] == 3 for pos in path[1:-1])
            if not has_monster:
                nearest_food = food
                break
            
    if nearest_food is None:
        return None

    return astar(matrix, pacman_position, nearest_food)



# Update Pacman's position based on the path found by A*
def update_pacman_position(matrix, pacman_position):
    path = find_path_to_nearest_food(matrix, pacman_position)
    # print(path)
    if path:
        next_position = path[1]  # Lấy vị trí thứ hai trong danh sách đường đi
        if matrix[next_position[0]][next_position[1]] == 3:  # Kiểm tra nếu Pacman chạm vào quái vật
            # Kết thúc trò chơi ở đây
            print("Game Over")
            return pacman_position
        else:
            matrix[pacman_position[0]][pacman_position[1]] = 0  # Xóa vị trí hiện tại của Pacman
            matrix[next_position[0]][next_position[1]] = 4  # Di chuyển Pacman đến vị trí tiếp theo
            return next_position
    
    return pacman_position

