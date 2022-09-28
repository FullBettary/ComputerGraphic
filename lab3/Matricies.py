import numpy as np

class Matrix:

    def __init__(self):
        #scale
        self.s_x = 30
        self.s_y = 30
        self.s_z = 30
    

    def inc_scale(self, scale, axies):
        if(axies == 'y'):
            self.s_x += scale
        elif(axies == 'z'):
            self.s_y += scale
        elif(axies == 'x'):
            self.s_z += scale

    def scale(self):
        return np.array([[self.s_x, 0, 0, 0],
                              [0, self.s_y, 0, 0],
                              [0, 0, self.s_z, 0],
                              [0, 0, 0, 1]])

    
    def rotation_x(self, a):
        #a = self.a_z
        return np.array([[np.cos(a), -np.sin(a), 0, 0],
                      [np.sin(a), np.cos(a), 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])


    def rotation_y(self, a):
        #a = self.a_x
        return np.array([[1, 0, 0, 0],
                      [0, np.cos(a), -np.sin(a), 0],
                      [0, np.sin(a), np.cos(a), 0],
                      [0, 0, 0, 1]])


    def rotation_z(self, a):
        #a = self.a_y
        return np.array([[np.cos(a), 0, np.sin(a), 0],
                      [0, 1, 0, 0],
                      [-np.sin(a), 0, np.cos(a), 0],
                      [0, 0, 0, 1]])

'''scale_m = np.array([[s_x, 0, 0, 0],
                              [0, s_y, 0, 0],
                              [0, 0, s_z, 0],
                              [0, 0, 0, 1]])'''



'''Rx = np.array([[1, 0, 0, 0],
                      [0, np.cos(a_x), -np.sin(a_x), 0],
                      [0, np.sin(a_x), np.cos(a_x), 0],
                      [0, 0, 0, 1]])'''

'''Ry = np.array([[np.cos(a_y), 0, np.sin(a_y), 0],
                      [0, 1, 0, 0],
                      [-np.sin(a_y), 0, np.cos(a_y), 0],
                      [0, 0, 0, 1]])'''

'''Rz = np.array([[np.cos(a_z), -np.sin(a_z), 0, 0],
                      [np.sin(a_z), np.cos(a_z), 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])'''
