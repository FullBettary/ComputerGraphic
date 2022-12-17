import pygame as pg
from HelperMetgod import *
from Consts import *
from copy import deepcopy


class MComplex:
    x = 0
    y = 0


def draw_set_of_Jule(sf):
    pix_arr = pg.PixelArray(sf)
    mx = pix_arr.shape[0]//2
    my = pix_arr.shape[1]//2
    z, t, c = MComplex(), MComplex(), MComplex()
    Max = 16
    iter = 50

    for y in range(-my, my):
        for x in range(-mx, mx):
            n = 2
            c.x = x * 0.004
            c.y = y * 0.004
            z.x = 0
            z.y = 0

            while z.x**2 + z.y**2 < Max and n < iter:
                t = deepcopy(z)
                z.x = t.x**3 - 3 * t.y**2 * t.x + c.x
                z.y = 3 * t.x**2 * t.y - t.y**3 + c.y
                n += 1
            if n < iter:
                pix_arr[mx + x][my + y] = rgb_to_int(LIST_OF_COLOR[3 - (n % 4)])
            else:
                pix_arr[mx + x][my + y] = rgb_to_int(BLACK)



