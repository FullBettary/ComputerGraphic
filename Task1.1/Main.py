from tkinter import *
from Line import SimpleLine
from Star import LineStar
from Rectangel import Rect
from Triangle import Trian
from Oval import oval
from Sector import Sec
from DashButton import dashButton
from ColorButton import colorButton
from ColorButtonExtend import extendColorButton

WIDTH = 1000
HEIGHT = 600

def move(event):
    x = event.x
    y = event.y
    s = "Движение мышью {}x{}".format(x, y)
    root.title(s)


root = Tk()

f_right = Frame(root)
f_right.pack(side=RIGHT)
f_left = Frame(root)
f_left.pack(side=LEFT)

c = Canvas(f_left, width=WIDTH, height=HEIGHT, bg='white')
c.pack()
root.bind("<Motion>", move)

line = SimpleLine(c)
Label(f_right, text='Линия').pack(side=TOP)
dashButton(f_right, line.get_line)
colorButton(f_right, line.get_line)

star = LineStar(c)
Label(f_right, text='Звезда').pack(side=TOP)
dashButton(f_right, star.get_star)
colorButton(f_right, star.get_star)

rect = Rect(c)
Label(f_right, text='Прямоугольник').pack(side=TOP)
dashButton(f_right, rect.get_rect)
extendColorButton(f_right, rect.get_rect)

triangle = Trian(c)
Label(f_right, text='Треугольник').pack(side=TOP)
dashButton(f_right, triangle.get_triangle)
extendColorButton(f_right, triangle.get_triangle)

oval = oval(c)
Label(f_right, text='Овал').pack(side=TOP)
dashButton(f_right, oval.get_oval)
extendColorButton(f_right, oval.get_oval)

sector = Sec(c)
Label(f_right, text='Сектор').pack(side=TOP)
dashButton(f_right, sector.get_sector)
extendColorButton(f_right, sector.get_sector)


line.get_line()
star.get_star()
rect.get_rect()
triangle.get_triangle()
oval.get_oval()
sector.get_sector()



root.mainloop()
