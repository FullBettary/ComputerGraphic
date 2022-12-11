def get_equation_for_surface_by_point(list_of_point):
    x0 = list_of_point[0][0]
    y0 = list_of_point[0][1]
    z0 = list_of_point[0][2]

    a2 = list_of_point[1][0] - x0
    a3 = list_of_point[2][0] - x0

    b2 = list_of_point[1][1] - y0
    b3 = list_of_point[2][1] - y0

    c2 = list_of_point[1][2] - z0
    c3 = list_of_point[2][2] - z0

    return lambda x, y: -1 * (x * (b2 * c3 - b3 * c2) + y * (c2 * a3 - a2 * c3) + x0 * (b3 * c2 - b2 * c3) + y0 * (
            a2 * c3 - a3 * c2) + z0 * (a3 * b2 - a2 * b3)) / (a2 * b3 - a3 * b2)


def distance(a, b):
    d = 0
    for i in range(len(a)):
        d += (a[i] - b[i]) ** 2
    return d ** 0.5


def exist_triangle(a, b, c):
    ab_l = distance(a, b)
    ac_l = distance(a, c)
    bc_l = distance(b, c)
    return ab_l + bc_l > ac_l and ab_l + ac_l > bc_l and bc_l + ac_l > ab_l


def int_to_rgb(int_rgb):
    return int_rgb // 256 // 256 % 256, int_rgb // 256 % 256, int_rgb % 256


def rgb_to_int(color):
    return color[0] * 256 ** 2 + color[1] * 256 + color[2]
