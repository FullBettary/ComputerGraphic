import pygame as pg
from Consts import BLACK


class Draw_poly:

    def __int__(self):
        pass

    @staticmethod
    def draw_poly(sf, poly):
        l = poly.get_list()
        if len(l) > 1:
            for i in range(len(l) - 1):
                pg.draw.line(sf, BLACK, l[i], l[i + 1], width=3)
        for i in l:
            pg.draw.circle(sf, BLACK, i, radius=3)
