import pygame as pg
import sys
from math import cos, sin 

def get_coord(t):
    around = 6
    radius = 62.5
    return (round(cos(t) * radius, around), round(sin(t) * radius, around))


HEIGHT = 250
WIDTH = 250
FPS = 60

RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pg.time.Clock()

sc = pg.display.set_mode((WIDTH, HEIGHT))


t = 0
step = 0.03
delta = 0.001
shift = 125


while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            sys.exit()

    keys = pg.key.get_pressed()

    if keys[pg.K_COMMA]:
        step -= delta
        
    elif keys[pg.K_PERIOD]:
        step += delta

    sc.fill(BLACK)

    coord = get_coord(t)
    t += step
        
    pg.draw.circle(sc, RED, (coord[0] + shift, coord[1] + shift), 10)
        
    pg.display.update()
    
    clock.tick(FPS)
