import pygame as pg
import sys
from Consts import *
from Polygon import Polygon
from Draw_poly import Draw_poly
from Filling import Filling

clock = pg.time.Clock()
current_poly = None
DP = Draw_poly()

fill = False

poly_list = []

surface = pg.display.set_mode(SIZE_WIN)

surface.fill(BACKGROUND)

while True:

    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_n and current_poly is None:
                p = Polygon()
                poly_list.append(p)
                current_poly = p
                fill = False
            elif i.key == pg.K_c:
                poly_list.clear()
                current_poly = None
                surface.fill(BACKGROUND)
            elif i.key == pg.K_f:
                fill = not fill
        elif i.type == pg.MOUSEBUTTONDOWN:
            if not fill:
                if current_poly is not None:
                    if i.button == 1:
                        pos = pg.mouse.get_pos()
                        current_poly.add_point(pos[0], pos[1])
                    elif i.button == 3:
                        current_poly.close_line()
                        current_poly = None
            else:
                if i.button == 1:
                    pos = pg.mouse.get_pos()
                    Filling.fill(surface, pos[0], pos[1])

    for poly in poly_list:
        DP.draw_poly(surface, poly)

    pos = pg.mouse.get_pos()
    pg.display.set_caption(f"x: {pos[0]} y: {pos[1]}   ({'Заливка' if fill else 'Полигон'})")

    pg.display.update()
    clock.tick(FPS)
