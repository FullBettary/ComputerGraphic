import pygame as pg
from SIF import *
from random import uniform, random
from HelperFunctions import *
from Consts import SIZE, GREEN


def draw(sf):

    pix_arr = pg.PixelArray(sf)
    iter = 3 * 10**5
    mx = 500
    my = -30
    rad = 70
    x, y = 0, 0

    for i in range(iter):
        if pg.QUIT in pg.event.get():
            return
        p = random()
        t = x
        if p >= 0.21:
            x = DRAGON['p1']['a1'] * x + DRAGON['p1']['b1'] * y + DRAGON['p1']['e1']
            y = DRAGON['p1']['c1'] * t + DRAGON['p1']['d1'] * y + DRAGON['p1']['f1']
        else:
            x = DRAGON['p2']['a2'] * x + DRAGON['p2']['b2'] * y + DRAGON['p2']['e2']
            y = DRAGON['p2']['c2'] * t + DRAGON['p2']['d2'] * y + DRAGON['p2']['f2']

        xi = int(mx + round(rad * x))
        yi = int(my - round(rad * y))

        pix_arr[xi][yi] = rgb_to_int(GREEN)  # list_color[int(uniform(0, len(list_color) - 1))]


