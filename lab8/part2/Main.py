import pygame as pg
import sys
from Consts import *
from AdditionalMethods import *
from Floating_horizont import floating_horizont


surface = pg.display.set_mode(SIZE_WIN2)

surface.fill(BACKGROUND)

clock = pg.time.Clock()

coord_axis(surface)

pg.display.update()

floating_horizont(surface)

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    pg.display.update()
    clock.tick(FPS)