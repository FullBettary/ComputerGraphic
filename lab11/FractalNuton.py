import pygame as pg
from Consts import *
from HelperMetgod import *
from copy import deepcopy


class MComplex:
    x = 0
    y = 0


def draw_fractal_Nuton(sf):
    pix_arr = pg.PixelArray(sf)

    ITER = 50
    MAX = 10 ** 6
    MIN = 10 ** -6

    mx = pix_arr.shape[0]//2
    my = pix_arr.shape[1]//2

    z = MComplex()
    scale = 0.005

    for y in range(-my, my):
        for x in range(-mx, mx):
            n = 0
            z.x = x * scale
            z.y = y * scale
            d = deepcopy(z)

            while z.x**2 + z.y**2 < MAX and d.x**2 + d.y**2 > MIN and n < ITER:
                t = deepcopy(z)
                p = (t.x**2 + t.y**2)**2
                z.x = 2 / 3 * t.x + (t.x**2 - t.y**2) / (3 * p)
                z.y = 2 / 3 * t.y * (1 - t.x / p)
                d.x = abs(t.x - z.x)
                d.y = abs(t.y - z.y)
                n += 1
            m = len(lc)
            pix_arr[mx + x][my + y] = rgb_to_int(lc[(m - 1) - (n % m)])
