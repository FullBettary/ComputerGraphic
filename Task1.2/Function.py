from math import log, sin, cos, inf, pi
from tkinter import *

class DrawFunc(Tk):

    def func1(self, x):
        if x == 1:
            return inf
        return (x * sin(3 * x)) / log(x)

    def cardioida(self, t):
        x = 4 * cos(t) * (1 + cos(t))
        y = 4 * sin(t) * (1 + cos(t))
        return (x, y)

    def __init__(self, root, func, color='red'):
        self.root = root
        self.scalar = 20
        self.color = color
        self.step = 0.01
        
        if(func == 1): self.drawFunc1()
        elif(func == 2): self.drawCardioida()
        
        

    def drawFunc1(self):
        i = self.step
        while(i <= 20):
            x1, x2 = i if i != 1 else i+self.step, i+self.step if i+self.step != 1 else i
            y1, y2 = round(self.func1(x1), 2), round(self.func1(x2), 2)
            i += self.step
            y1 = -1 * y1 * self.scalar + 300
            y2 = -1 * y2 * self.scalar + 300
            x1 = x1 * self.scalar + 500
            x2 = x2 * self.scalar + 500

            self.root.create_line(x1, y1, x2, y2, width=2, fill=self.color)


    def drawCardioida(self):
        i = self.step - self.step

        while(i < 2 * pi - self.step):
            first_pair = self.cardioida(i)
            second_pair = self.cardioida(i + self.step)
            i += self.step
            x1, x2 = first_pair[0], second_pair[0]
            y1, y2 = first_pair[1], second_pair[1]

            y1 = -1 * y1 * self.scalar + 300
            y2 = -1 * y2 * self.scalar + 300
            x1 = x1 * self.scalar + 500
            x2 = x2 * self.scalar + 500

            self.root.create_line(x1, y1, x2, y2, width=2, fill=self.color)
            


