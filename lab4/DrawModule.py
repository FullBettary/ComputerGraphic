import numpy as np
import pygame as pg
from CONST import BLACK
from Matricies import *

class draw_mudule:
    
    def __init__(self, obj, sf):
        self.draw_obj = obj
        self.sf = sf
        shift_x = sf.get_width()/2
        shift_y = sf.get_height()/2
        self.to_begin_coord_mtr = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [shift_x, shift_y, 0, 1]])


    def draw(self, matr_rot=np.eye(4), matr_shift=np.eye(4)):

        fig = self.draw_obj.get_coord()
        
        fig = fig.dot(scale())
        fig = fig.dot(matr_shift)
        fig = fig.dot(matr_rot)
        fig = fig.dot(izometria())
        fig = fig.dot(self.to_begin_coord_mtr)
        
        for pair in self.draw_obj.get_pair_coord():
            p1, p2 = pair[0], pair[1]
            x1, y1, x2, y2 = fig[p1, 0], fig[p1, 1], fig[p2, 0], fig[p2, 1]

            pg.draw.line(self.sf, BLACK, (x1, y1), (x2, y2), 2)
        
