class FastClip:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def __in_five_zone(self, x, y):
        return (self.__x1 <= x <= self.__x2) and (self.__y1 <= y <= self.__y2)

    def __get_x(self, point_a, point_b, p):
        return point_a[0] + ((p - point_a[1]) * (point_b[0] - point_a[0])) / (point_b[1] - point_a[1])

    def __get_y(self, point_a, point_b, p):
        return point_a[1] + ((p - point_a[0]) * (point_b[1] - point_a[1])) / (point_b[0] - point_a[0])

    def clip(self, point_a, point_b):

        if self.__in_five_zone(point_a[0], point_a[1]) and self.__in_five_zone(point_b[0], point_b[1]):
            return [point_a, point_b]

        res = []
        points = [point_a, point_b]

        for point in points:
            if point[0] < self.__x1 and point[1] < self.__y1: # check 1 zone
                x = self.__get_x(point_a, point_b, self.__y1) # top side
                if self.__in_five_zone(x, self.__y1):
                    res.append([x, self.__y1])
                else:
                    y = self.__get_y(point_a, point_b, self.__x1) # left side
                    if self.__in_five_zone(self.__x1, y):
                        res.append([self.__x1, y])

            elif self.__x1 < point[0] < self.__x2 and point[1] < self.__y1: # check 2 zone
                x = self.__get_x(point_a, point_b, self.__y1)
                if self.__in_five_zone(x, self.__y1):
                    res.append([x, self.__y1])

            elif self.__x2 < point[0] and point[1] < self.__y1: # check 3 zone
                x = self.__get_x(point_a, point_b, self.__y1) # top side
                if self.__in_five_zone(x, self.__y1):
                    res.append([x, self.__y1])
                else:
                    y = self.__get_y(point_a, point_b, self.__x2) # right side
                    if self.__in_five_zone(self.__x1, y):
                        res.append([self.__x1, y])

            elif point[0] < self.__x1 and self.__y1 < point[1] < self.__y2: # check 4 zone
                y = self.__get_y(point_a, point_b, self.__x1)  # left side
                if self.__in_five_zone(self.__x1, y):
                    res.append([self.__x1, y])

            elif self.__x2 < point[0] and self.__y1 < point[1] < self.__y2: # check 6 zone
                y = self.__get_y(point_a, point_b, self.__x2)  # right side
                if self.__in_five_zone(self.__x1, y):
                    res.append([self.__x1, y])

            elif point[0] < self.__x1 and point[1] < self.__y2: # check 7 zone
                x = self.__get_x(point_a, point_b, self.__y2)  # bottom side
                if self.__in_five_zone(x, self.__y1):
                    res.append([x, self.__y1])
                else:
                    y = self.__get_y(point_a, point_b, self.__x1)  # left side
                    if self.__in_five_zone(self.__x1, y):
                        res.append([self.__x1, y])

            elif self.__x1 < point[0] < self.__x2 and self.__y2 < point[1]: # check 8 zone
                x = self.__get_x(point_a, point_b, self.__y2)  # bottom side
                if self.__in_five_zone(x, self.__y1):
                    res.append([x, self.__y1])

            elif self.__x2 < point[0] and self.__y2 < point[1]: # check 9 zone
                x = self.__get_x(point_a, point_b, self.__y2)  # bottom side
                if self.__in_five_zone(x, self.__y1):
                    res.append([x, self.__y1])
                else:
                    y = self.__get_y(point_a, point_b, self.__x2) # right side
                    if self.__in_five_zone(self.__x1, y):
                        res.append([self.__x1, y])
            else: # else 5 zone
                res.append(list(point))

        if len(res) == 1: # if have one point on board
            res = []

        s_x = self.__x1
        s_y = self.__y1
        for i in range(len(res)):
            res[i][0] -= s_x
            res[i][1] -= s_y

        return res