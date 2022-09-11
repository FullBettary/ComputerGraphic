from tkinter import *
from Function import DrawFunc

WIDTH = 1000
HEIGHT = 600

def drawGrind(c):
    c.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill='black', width=3)
    c.create_line(0, HEIGHT/2, WIDTH, HEIGHT/2, fill='black', width=3)
    counter = 0
    while(counter <= WIDTH):
        c.create_line(0, counter, WIDTH, counter, fill='black', width=1)
        c.create_line(counter, 0, counter, HEIGHT, fill='black', width=1)
        counter += 10

def helper(c, func, n):
    func(c, n, 'white')
    drawGrind(c)

root = Tk()

right_frame = Frame(root)
right_frame.pack(side=RIGHT)
left_frame = Frame(root)
left_frame.pack(side=LEFT)

c = Canvas(left_frame, width=WIDTH, height=HEIGHT, bg='white')
c.pack()

drawGrind(c)

Button(right_frame, text='Начертить \nграфик', command=lambda : DrawFunc(c, 1, 'blue')).pack(side=TOP)
Button(right_frame, text='Стереть \nграфик', command=lambda : helper(c, DrawFunc, 1)).pack(side=TOP)

Button(right_frame, text='Начертить \nкардиоиду', command=lambda : DrawFunc(c, 2)).pack(side=TOP)
Button(right_frame, text='Стереть \nкардиоиду', command=lambda : helper(c, DrawFunc, 2)).pack(side=TOP)

mainloop()
