import pygame as pg
from part1.Moduls import rgb_to_int
from part1.Consts import *


def show(sf, figures, euq):
    pix_arr = pg.PixelArray(sf)
    colors = [rgb_to_int(RED), rgb_to_int(BLUE)]

    figs = []
    for fig in figures:
        f = []
        for point in fig:
            f.append(point[0:2])
        figs.append(f)

    canvas = pg.Surface(pix_arr.shape)
    z_buffer = [[{'value': -1 * 10**6, 'color': -1} for i in range(pix_arr.shape[1])] for i in range(pix_arr.shape[0])]

    for i in range(len(figs)):
        canvas.fill(BACKGROUND)
        pg.draw.polygon(canvas, BLACK, figs[i])
        pxar = pg.PixelArray(canvas)
        for x in range(pxar.shape[0]):
            for y in range(pxar.shape[1]):
                if pxar[x][y] == rgb_to_int(BLACK):
                    if euq[i](x, y) > z_buffer[x][y]['value']:
                        z_buffer[x][y]['value'] = euq[i](x, y)
                        z_buffer[x][y]['color'] = colors[i]

    for x in range(len(z_buffer)):
        for y in range(len(z_buffer[0])):
            if z_buffer[x][y]['color'] != -1:
                pix_arr[x][y] = z_buffer[x][y]['color']

    pg.display.update()