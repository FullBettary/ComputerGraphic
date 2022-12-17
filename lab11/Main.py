import pygame as pg
import sys
from Consts import *
from SetOfMandelbord import *
from SetOfJule import *
from FractalNuton import *

surface = pg.display.set_mode(SIZE)
clock = pg.time.Clock()

surface.fill(BACKGROUND)

surface_list = [pg.Surface(SIZE), pg.Surface(SIZE), pg.Surface(SIZE)]
current_sf = surface_list[0]

pg.display.update()

draw_set_of_Mandelbord(surface_list[0])
draw_set_of_Jule(surface_list[1])
draw_fractal_Nuton(surface_list[2])
pg.display.set_caption('Фракталы построены')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                current_sf = surface_list[0]
                pg.display.set_caption('Множество Мондельборта')
            elif event.key == pg.K_2:
                current_sf = surface_list[1]
                pg.display.set_caption('Множество Жюлиа')
            elif event.key == pg.K_3:
                current_sf = surface_list[2]
                pg.display.set_caption('Фрактал Ньютона')

    surface.blit(current_sf, dest=(0, 0))
    pg.display.update()
    clock.tick(FPS)
