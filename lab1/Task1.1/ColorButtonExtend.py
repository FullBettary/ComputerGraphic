from ColorButton import colorButton
from tkinter import *

class extendColorButton(colorButton, Tk):

    def __init__(self, root, target_func):
        super().__init__(root, target_func)
        self.frame2 = Frame(self.frame)
        self.frame2.pack(side=BOTTOM)

        Button(self.frame2, bg='#ff0000', command = lambda : self.target_func(fill = 'red')).pack(side=LEFT)
        Button(self.frame2, bg='#00FF00', command = lambda : self.target_func(fill = 'green')).pack(side=LEFT)
        Button(self.frame2, bg='#FFFF00', command = lambda : self.target_func(fill = 'yellow')).pack(side=LEFT)
        Button(self.frame2, bg='#ffffff', command = lambda : self.target_func(fill = 'white')).pack(side=LEFT)

        
