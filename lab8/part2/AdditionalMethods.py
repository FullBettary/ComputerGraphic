import pygame as pg
from Consts import COLORS_AXIS, SIZE_WIN2 as SIZE
from Matrices import izometria, moveXY
import numpy as np


def coord_axis(sf):
    length = 400
    line1 = np.array([-length, 0, 0, 1])
    line2 = np.array([0, -length, 0, 1])
    line3 = np.array([0, 0, -length, 1])
    axis = np.array([line1, line2, line3])

    axis = axis.dot(izometria()).dot(moveXY(SIZE[0]//2, SIZE[1]//2))

    for i in range(len(axis)):
        pg.draw.line(sf, COLORS_AXIS[i], (SIZE[0]//2, SIZE[1]//2), axis[i][0:2], 3)
