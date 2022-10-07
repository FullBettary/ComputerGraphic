import pygame as pg
import sys

from CONST import *
from Tetraeder import Tetr
from DrawModule import draw_mudule
from Matricies import *


SIZE = 500
FPS = 60

surface = pg.display.set_mode((SIZE, SIZE))
clock = pg.time.Clock()
surface.fill(LIGHT_GREY)

ttr = Tetr()
dm = draw_mudule(ttr, surface)

step = 0.025
alpha = step

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            sys.exit()

    surface.fill(LIGHT_GREY)

    dm.draw(Ry(alpha), moveXY(100, 100))
    alpha += step

    pg.display.update()
    
    clock.tick(FPS)
