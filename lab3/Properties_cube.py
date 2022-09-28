import numpy as np
import pygame as pg

from CONST import *

class Cube:

    def __init__(self):
        self.vertex = np.array([[1, -1, 1, 1],
                           [-1, -1, 1, 1],
                           [-1, 1, 1, 1],
                           [1, 1, 1, 1],
                           [1, -1, -1, 1],
                           [-1, -1, -1, 1],
                           [-1, 1, -1, 1],
                           [1, 1, -1, 1]])

        self.pair_ver = [[0, 1],
                [1, 2],
                [2, 3],
                [3, 0],
            
                [4, 5],
                [5, 6],
                [6, 7],
                [7, 4],
            
                [0, 4],
                [1, 5],
                [2, 6],
                [3, 7]]

        self.shift_x = WIN_W/2
        self.shift_y = WIN_H/2
        

    def draw_cube(self, surface, ratation=None, scale=None):
        if not np.array_equal(ratation, None):
            self.vertex = self.vertex.dot(ratation)

        v = self.vertex
        
        if not np.array_equal(scale, None):
            v = v.dot(scale)

        #v = self.vertex
    
        for i in self.pair_ver:
            x1, y1, x2, y2 = v[i[0], 0], v[i[0], 1], v[i[1], 0], v[i[1], 1] 
            pg.draw.line(surface, 'BLACK', (x1 + self.shift_x, y1 + self.shift_y), (x2 + self.shift_x, y2 + self.shift_y), 2)
        
