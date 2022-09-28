import sys
import pygame as pg
import numpy as np

import Matricies as M
import Properties_cube as CUBE 
from CONST import *

main_sf = pg.display.set_mode(SIZE)
clock = pg.time.Clock()

main_sf.fill(LIGHT_GREY)


C = CUBE.Cube()
M = M.Matrix()

C.draw_cube(main_sf, None, M.scale())

pg.display.update()

while STATUS:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            sys.exit()

    keys = pg.key.get_pressed()

    if keys[pg.K_1]:
        if keys[pg.K_LEFT]:
            main_sf.fill(LIGHT_GREY)
            C.draw_cube(main_sf, M.rotation_x(0.005), M.scale())
            pg.display.update()
        if keys[pg.K_RIGHT]:
            main_sf.fill(LIGHT_GREY)
            C.draw_cube(main_sf, M.rotation_x(-0.005), M.scale())
            pg.display.update()


    if keys[pg.K_2]:
        if keys[pg.K_LEFT]:
            main_sf.fill(LIGHT_GREY)
            C.draw_cube(main_sf, M.rotation_y(0.005), M.scale())
            pg.display.update()
        if keys[pg.K_RIGHT]:
            main_sf.fill(LIGHT_GREY)
            C.draw_cube(main_sf, M.rotation_y(-0.005), M.scale())
            pg.display.update()
        if keys[pg.K_p]:
            M.inc_scale(1, 'y')
            main_sf.fill(LIGHT_GREY)
            C.draw_cube(main_sf, None, M.scale())
            pg.display.update()
        if keys[pg.K_m]:
            M.inc_scale(-1, 'y')
            main_sf.fill(LIGHT_GREY)
            C.draw_cube(main_sf, None, M.scale())
            pg.display.update()


    if keys[pg.K_3]:
        if keys[pg.K_LEFT]:
            main_sf.fill(LIGHT_GREY)
            C.draw_cube(main_sf, M.rotation_z(0.005), M.scale())
            pg.display.update()
        if keys[pg.K_RIGHT]:
            main_sf.fill(LIGHT_GREY)
            C.draw_cube(main_sf, M.rotation_z(-0.005), M.scale())
            pg.display.update()
        if keys[pg.K_p]:
            M.inc_scale(1, 'z')
            main_sf.fill(LIGHT_GREY)
            C.draw_cube(main_sf, None, M.scale())
            pg.display.update()
        if keys[pg.K_m]:
            M.inc_scale(-1, 'z')
            main_sf.fill(LIGHT_GREY)
            C.draw_cube(main_sf, None, M.scale())
            pg.display.update()
       

    clock.tick(FPS)
            
