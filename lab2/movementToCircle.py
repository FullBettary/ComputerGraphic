import pygame as pg
import sys
import numpy as np
from math import cos, sin 

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

to_local_begin_coord = np.array([[1, 0, 0],
                                                [0, 1, 0],
                                                [shift, shift, 1]])

d = np.array([[1, 0, 0],
                    [0, 1, 0],
                    [50, 50, 1]])

coord = np.array([0, 0, 1])

STATUS = True

while STATUS:
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

    rotation = np.array([[cos(t), sin(t), 0], [-sin(t), cos(t), 0], [0, 0, 1]])
    
    c = coord.dot(d).dot(rotation).dot(to_local_begin_coord)
    
    t += step
        
    pg.draw.circle(sc, RED, (c[0], c[1]), 10)
        
    pg.display.update()
    
    clock.tick(FPS)
