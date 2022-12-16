import pygame as pg
from Consts import *
from HelperMethod import *
from Consts import *


def draw(sf, point1, point2, point3, n):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    x3, y3 = point3[0], point3[1]
    if n > 0:
        x1n = (x1 + x2) // 2
        y1n = (y1 + y2) // 2
        x2n = (x2 + x3) // 2
        y2n = (y2 + y3) // 2
        x3n = (x3 + x1) // 2
        y3n = (y3 + y1) // 2
        pg.draw.polygon(sf, BACKGROUND, [(x1n, y1n), (x2n, y2n), (x3n, y3n)])
        draw(sf, (x1, y1), (x1n, y1n), (x3n, y3n), n - 1)
        draw(sf, (x2, y2), (x1n, y1n), (x2n, y2n), n - 1)
        draw(sf, (x3, y3), (x2n, y2n), (x3n, y3n), n - 1)


def draw_triangle_Serpincky(sf, n):
    point1 = (100, 500)
    point2 = (500, 500)
    point3 = (300, 154)
    iter = n
    pg.draw.polygon(sf, BLUE, (point1, point2, point3))
    draw(sf, point1, point2, point3, iter)
