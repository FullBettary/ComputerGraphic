from ConditionFigure import Figure
from tkinter import *

class SimpleLine(Figure):

    def get_line(self, type_line=None, border_color=None):
        self.dash_cond = self.dash_cond if type_line == None else ((10, 2) if type_line == True else None)
        self.board_color = self.board_color if border_color == None else border_color
        
        self.root.create_line(10, 10, 500, 50, fill='white', width=5)
        self.root.create_line(10, 10, 500, 50, dash=self.dash_cond, fill=self.board_color, width=5)  # simple line
