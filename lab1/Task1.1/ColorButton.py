from tkinter import *

class colorButton(Tk):
    def __init__(self, root, target_func):
        self.root = root
        self.target_func = target_func
        
        self.frame = Frame(self.root)
        self.frame1 = Frame(self.root)
        self.frame.pack(side=TOP)
        self.frame1.pack(side=TOP)
        
        Button(self.frame1, bg='#ff0000', command = lambda : self.target_func(border_color = 'red')).pack(side=LEFT)
        Button(self.frame1, bg='#00FF00', command = lambda : self.target_func(border_color = 'green')).pack(side=LEFT)
        Button(self.frame1, bg='#FFFF00', command = lambda : self.target_func(border_color = 'yellow')).pack(side=LEFT)
        Button(self.frame1, bg='#000000', command = lambda : self.target_func(border_color = 'black')).pack(side=LEFT)
