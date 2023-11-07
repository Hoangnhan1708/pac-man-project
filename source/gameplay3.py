import pygame
import heapq
import random
import numpy as np
import extract
#def move_pacman_randomly(pacman_position):

    #return pacman_position

# Get Pacman vision range 3x3
def pacman_vision(matrix, pacman_position):
    pacman_vision_matrix = np.zeros((7, 7), dtype = int)
    range =  [0 , 1, -1, 2 , -2, 3, -3]
    
    for i in range:
        for j in range:
            if 0 <= pacman_position[0] + i < len(pacman_vision_matrix) and 0 <= pacman_position[1] + j < len(pacman_vision_matrix):
                pacman_vision_matrix[pacman_position[0] + i, pacman_position[1] + j] = matrix[pacman_position[0] + i, pacman_position[1] + j]
            else:
                break
    
    return pacman_vision_matrix

def reachables(pacman_vision):
    pass

def path(pacma_vision, goal = None, random = True):
    pass

