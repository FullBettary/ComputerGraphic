import pygame as pg
from random import random
from Consts import BLACK
from IFS import *
from HelperMethod import *


def draw_curve_Koch(sf):
    pix_arr = pg.PixelArray(sf)

    iter = 40 * 10**5
    x, y = 0, 0
    mx = 50
    my = 200
    rad = 500

    for i in range(iter):
        p = random()
        t = x
        if p >= 0.21:
            x = curve_Koch['p1']['a'] * x + curve_Koch['p1']['b'] * y + curve_Koch['p1']['e']
            y = curve_Koch['p1']['c'] * t + curve_Koch['p1']['d'] * y + curve_Koch['p1']['f']
        else:
            x = curve_Koch['p2']['a'] * x + curve_Koch['p2']['b'] * y + curve_Koch['p2']['e']
            y = curve_Koch['p2']['c'] * t + curve_Koch['p2']['d'] * y + curve_Koch['p2']['f']

        px = mx + int(round(rad * x))
        py = my + int(round(rad * y))
        pix_arr[px][py] = rgb_to_int(BLACK)

    pg.display.update()


