import pygame as pg
import sys

WIDTH, HEIGHT = 910, 650
SIZE = (WIDTH, HEIGHT)
LIGHT_GREY = (160, 160, 160)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 250, 0)
FPS = 60
pixel_size = 10

pg.font.init()
font = pg.font.Font(None, 15)

def draw_coord_axies():
    pg.draw.line(sf, BLACK, [0, 0], [WIDTH, 0], 2)
    pg.draw.line(sf, BLACK, [0, 0], [0, HEIGHT], 2)
    for i in range(0, WIDTH, pixel_size * 2):
        pg.draw.line(sf, BLACK, [i, 0], [i, 10], 2)
        text = font.render(f'{i // pixel_size}', True, BLACK)
        sf.blit(text, (i, 10))

    for i in range(0, HEIGHT, pixel_size):
        pg.draw.line(sf, BLACK, [0, i], [10, i], 2)
        text = font.render(f'{i // pixel_size}', True, BLACK)
        sf.blit(text, (10, i))

def draw_line(x1, y1, x2, y2):
    x1, y1, x2, y2 = x1 * pixel_size, y1 * pixel_size, x2 * pixel_size, y2 * pixel_size
    x, y = x1, y1
    dx, dy = (x2 - x1)//pixel_size, (y2 - y1)//pixel_size
    e = 2 * dx - dy
    for i in range(dy + 1):
        pg.draw.rect(sf, BLACK, (x, y, pixel_size, pixel_size))
        while e >= 0:
            x += pixel_size
            e -= 2 * dy
        e += 2 * dx
        y += pixel_size

def draw_circle(x, y, r):
    disp_x, disp_y, r = x * pixel_size, y * pixel_size, r * pixel_size
    x, y = 0, r
    delta = 1 - 2 * r
    error = 0
    while y >= 0:
        pg.draw.rect(sf, BLACK, (disp_x + x, disp_y + y, pixel_size, pixel_size))
        pg.draw.rect(sf, BLACK, (disp_x + x, disp_y - y, pixel_size, pixel_size))
        pg.draw.rect(sf, BLACK, (disp_x - x, disp_y + y, pixel_size, pixel_size))
        pg.draw.rect(sf, BLACK, (disp_x - x, disp_y - y, pixel_size, pixel_size))

        error = 2 * (delta + y) - 1
        if delta < 0 and error <= 0:
            x += pixel_size
            delta += 2 * x + 1
            continue
        error = 2 * (delta - x) - 1
        if delta > 0 and error > 0:
            y -= pixel_size
            delta += 1 - 2 * y
            continue
        x += pixel_size
        delta += 2 * (x - y)
        y -= pixel_size

sf = pg.display.set_mode(SIZE)
clock = pg.time.Clock()

flag = False

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            sys.exit()

    sf.fill(LIGHT_GREY)

    draw_coord_axies()
    draw_line(10, 14, 20, 30)
    draw_circle(60, 50, 9)

    mouse_pos = pg.mouse.get_pos()
    pg.draw.line(sf, BLACK, [0, mouse_pos[1]], [WIDTH, mouse_pos[1]], 1)
    pg.draw.line(sf, BLACK, [mouse_pos[0], 0], [mouse_pos[0], HEIGHT], 1)

    pg.display.update()
    clock.tick(FPS)