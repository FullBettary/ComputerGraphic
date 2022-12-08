class Polygon:
    def __init__(self):
        self.__point_list = []
        self.__close = False

    def add_point(self, x, y):
        if not self.__close:
            self.__point_list.append((x, y))

    def close_line(self):
        if not self.__close:
            self.__point_list.append(self.__point_list[0])
            self.__close = True

    def get_list(self):
        return self.__point_list
