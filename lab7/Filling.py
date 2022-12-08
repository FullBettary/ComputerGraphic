import pygame as pg
from Consts import *


class Filling:
    def __init__(self):
        pass

    @staticmethod
    def __int_to_rgb(int_rgb):
        return int_rgb // 256 // 256 % 256, int_rgb // 256 % 256, int_rgb % 256

    @staticmethod
    def __rgb_to_int(color):
        return color[0] * 256**2 + color[1] * 256 + color[2]

    @staticmethod
    def fill(sf, x, y):
        pix_arr = pg.PixelArray(sf)
        suspicious_point = []

        if Filling.__int_to_rgb(pix_arr[x][y]) == BLACK or Filling.__int_to_rgb(pix_arr[x][y]) == RED:
            return

        j = x
        while pix_arr[j][y] != Filling.__rgb_to_int(BLACK):
            pix_arr[j][y] = Filling.__rgb_to_int(RED)
            if pix_arr[j][y + 1] != Filling.__rgb_to_int(RED) or pix_arr[j][y + 1] != Filling.__rgb_to_int(BLACK):
                suspicious_point.append((j, y + 1))
            if pix_arr[j][y - 1] != Filling.__rgb_to_int(RED) or pix_arr[j][y - 1] != Filling.__rgb_to_int(BLACK):
                suspicious_point.append((j, y - 1))
            j += 1

        j = x - 1
        while pix_arr[j][y] != Filling.__rgb_to_int(BLACK):
            pix_arr[j][y] = Filling.__rgb_to_int(RED)
            if pix_arr[j][y + 1] != Filling.__rgb_to_int(RED) or pix_arr[j][y + 1] != Filling.__rgb_to_int(BLACK):
                suspicious_point.append((j, y + 1))
            if pix_arr[j][y - 1] != Filling.__rgb_to_int(RED) or pix_arr[j][y - 1] != Filling.__rgb_to_int(BLACK):
                suspicious_point.append((j, y - 1))
            j -= 1

        pg.display.update()

        Filling.fill(sf, x, y + 1)
        Filling.fill(sf, x, y - 1)

        for i in suspicious_point:
            Filling.fill(sf, i[0], i[1])



