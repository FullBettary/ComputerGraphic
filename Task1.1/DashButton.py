from tkinter import *

class dashButton(Tk):
    
    def __init__(self, root, target_func):
        self.root = root
        self.target_func = target_func

        Button(self.root, text='Пунктир', command=lambda : self.target_func(type_line = True)).pack(side=TOP)
        Button(self.root, text='Сплошная', command=lambda : self.target_func(type_line = False)).pack(side=TOP)
