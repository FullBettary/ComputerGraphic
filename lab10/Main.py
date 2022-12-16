import pygame as pg
import sys
from Consts import *
from DrawCurveCoch import draw_curve_Koch
from TriangleSerpibcky import draw_triangle_Serpincky

main_surface = pg.display.set_mode(MAIN_SIZE)

clock = pg.time.Clock()

main_surface.fill(BACKGROUND)
pg.display.update()

surface1 = pg.Surface(SIZE)
surface1.fill(BACKGROUND)

draw_curve_Koch(surface1)
main_surface.blit(surface1, dest=(0, 0))
pg.display.update()

surface2 = pg.Surface(SIZE)
surface2.fill(BACKGROUND)

draw_triangle_Serpincky(surface2, 4)
main_surface.blit(surface2, dest=(WIN_W//2, 0))
pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pg.display.update()

    clock.tick(FPS)
