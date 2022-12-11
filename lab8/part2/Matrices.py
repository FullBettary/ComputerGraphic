from math import cos, sin, sqrt
from numpy import array


def rotation():
    return array([[1, 0, 0, 0], [0, cos(90), sin(90), 0], [0, -sin(90), cos(90), 0], [0, 0, 0, 1]])


def Rx(t):
    return array([[1, 0, 0, 0], [0, cos(t), sin(t), 0], [0, -sin(t), cos(t), 0], [0, 0, 0, 1]])


def Ry(t):
    return array([[cos(t), 0, -sin(t), 0], [0, 1, 0, 0], [sin(t), 0, cos(t), 0], [0, 0, 0, 1]])


def Rz(t):
    return array([[cos(t), sin(t), 0, 0], [-sin(t), cos(t), 0, 0], [0, 0, 1, 0], [0, 0, 0,1]])


def moveXY(shift_x, shift_y):
    return array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [shift_x, shift_y, 0, 1]])


def scale():
    s = 100
    return array([[s, 0, 0, 0], [0, s, 0, 0], [0, 0, s, 0],  [0, 0, 0, 1]])


def izometria():
    return array([[sqrt(2)/2, -sqrt(6)/6, sqrt(3)/3, 0],
                       [0, sqrt(2/3), sqrt(3)/3, 0],
                       [-sqrt(2)/2, -sqrt(6)/6, sqrt(3)/3, 0],
                       [0, 0, 0, 1]])