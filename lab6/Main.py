import pygame as pg
import sys
import CONSTS as const
from FastClipping import FastClip

surface = pg.display.set_mode(const.SIZE_MAIN_WIN)
windows = pg.Surface(const.SIZE_WIN)

clock = pg.time.Clock()
surface.fill(const.BLACK)
windows.fill(const.LIGHT_GREY)

fc = FastClip(const.X1_WIN, const.Y1_WIN, const.X2_WIN, const.Y2_WIN)
coord = fc.clip(const.POINT_A, const.POINT_B)

if len(coord) != 0:
    pg.draw.line(windows, const.RED, coord[0], coord[1], 3)

pg.draw.line(surface, const.GREEN, const.POINT_A, const.POINT_B, 3)

surface.blit(windows, (const.X1_WIN, const.Y1_WIN))

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pg.display.update()
    clock.tick(const.FPS)