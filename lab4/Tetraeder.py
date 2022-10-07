import numpy as np
from math import sqrt


class Tetr:
    def __init__(self):
        self.coord = np.array([[-0.5, 0, -0.5, 1],
                                        [0.5, 0, -0.5, 1],
                                        [0, 0, (sqrt(3)-1)/2, 1],
                                        [0, -sqrt(12)/6, (sqrt(3) - 3)/6, 1]])

        self.pair_coord = [[0, 1],
                                  [0, 2],
                                  [0, 3],
                                  [2, 1],
                                  [2, 3],
                                  [3, 1]]

    def get_coord(self):
        return self.coord

    def get_pair_coord(self):
        return self.pair_coord
