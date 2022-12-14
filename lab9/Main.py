import pygame as pg
import sys
from Consts import *
import DrawFractal

surface = pg.display.set_mode(SIZE)

clock = pg.time.Clock()

surface.fill(BACKGROUND)

pg.display.update()

DrawFractal.draw(surface)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pg.display.update()
    clock.tick(FPS)
