import numpy as np
import pygame as pg
from Matrices import *
from Consts import SIZE_WIN2 as SIZE, BLUE
from Moduls import rgb_to_int

r = 30

y_coord = lambda x, z: np.round(np.sqrt(r * z - np.power(x, 2)))

x_coord = lambda y, z: np.round(np.sqrt(r * z - np.power(y, 2)))


def floating_horizont(sf):
    coord = []

    for z in range(0, 300, 10):
        for x in range(0, int(np.round(np.sqrt(r * z + 1)))):
            y = y_coord(x, z)
            coord.append([x, y, z, 1])
            coord.append([x, -y, z, 1])
            coord.append([-x, y, z, 1])
            coord.append([-x, -y, z, 1])

            coord.append([y, x, z, 1])
            coord.append([y, -x, z, 1])
            coord.append([-y, x, z, 1])
            coord.append([-y, -x, z, 1])

    coord = np.array(coord)
    coord = coord.dot(Rx(90))
    coord = coord.dot(moveXY(SIZE[0] // 2, SIZE[1] // 2))
    print(coord)

    pix_arr = pg.PixelArray(sf)

    for point in coord:
        x = int(point[0])
        y = int(point[1])

        if not (0 <= x < SIZE[0] and 0 <= y < SIZE[1]):
            continue

        pix_arr[x][y] = rgb_to_int(BLUE)

    pg.display.update()
