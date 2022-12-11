import sys
import pygame as pg
from part1 import InputMenu
import Moduls
from part1.Consts import *
import ZBuffer as zb

points = InputMenu.InputMenu()

z = []

for i in points:
    z.append(Moduls.get_equation_for_surface_by_point(i))

surface = pg.display.set_mode(SIZE_WIN)
clock = pg.time.Clock()

surface.fill(BACKGROUND)


pg.display.set_caption('')
pg.display.update()

surface = zb.show(surface, points, z)

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    clock.tick(FPS)


