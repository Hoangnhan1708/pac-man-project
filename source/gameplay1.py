import heapq
import extract
from pygame import event, QUIT, display
import render

# Heuristic function (h(x): estimated distance from processing location to goal)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Get neighbors of a given point
def get_neighbors(matrix, node):
    neighbors = []
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= node[0] + i < len(matrix) and 0 <= node[1] + j < len(matrix[0]) and matrix[node[0] + i][node[1] + j] != 1 :
            neighbors.append((node[0] + i, node[1] + j))
                
    return neighbors


# A* algorithm
def astar(matrix, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {start: None}
    g_score = {start: 0}
    pathAlter =[]
    while open_set:
        current = heapq.heappop(open_set)[1] 
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        # else:
        #     pathAlter.append(current)
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


    nearest_food = None
    for food in food_positions:
        path = astar(matrix, pacman_position, food)
        if path is not None:
            nearest_food = food
            
    if nearest_food is None:
        return None

    return astar(matrix, pacman_position, nearest_food)


# Update Pacman's position based on the path found by A*
def update_pacman_position(matrix, pacman_position):
    path = find_path_to_nearest_food(matrix, pacman_position)
    foodPosition = None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                foodPosition = (i,j)
    if path:
        next_position = path[1]  # Lấy vị trí thứ hai trong danh sách đường đi
        if matrix[next_position[0]][next_position[1]] == 3:  # Kiểm tra nếu Pacman chạm vào quái vật
            # Kết thúc trò chơi ở đây
            print("Game Over")
            return (-1,-1)
        else:
            matrix[pacman_position[0]][pacman_position[1]] = 5  # Đánh dấu lại vị trí mà Pacman đã đi qua
            matrix[next_position[0]][next_position[1]] = 4  # Di chuyển Pacman đến vị trí tiếp theo
            if (next_position[0],next_position[1]) == foodPosition :
                print("You Win")
                return (-1,-1)
            return next_position
    return pacman_position

def play(timer, screen):
    fps = 10
    run = True        
    matrix = extract.extractMatrix('map{}.txt'.format(1))
    player_location = extract.extractLocation('map{}.txt'.format(1))      
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
        if  (player_x, player_y) != (-1,-1):
            player_x, player_y = update_pacman_position(matrix, (player_x, player_y))
            score_value -= 1
            if score_value == 0:
                run = False
        else:
            run = False

        render.render(matrix)
        render.render_score(300,700,score_value)

        for eventElement in event.get():
            if eventElement.type == QUIT:
                    run = False   
        display.flip()     