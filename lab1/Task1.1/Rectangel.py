from ExtendConditionFigure import extendFigure

class Rect(extendFigure):

    def get_rect(self, type_line=None, fill=None, border_color=None):
        self.fill = self.fill if fill == None else fill
        self.board_color = self.board_color if border_color == None else border_color
        self.dash_cond = self.dash_cond if type_line == None else ((10, 2) if type_line == True else None)
    
        self.root.create_rectangle(70, 70, 500, 200, fill='white', outline='white', width=3)
        self.root.create_rectangle(70, 70, 500, 200, fill = self.fill, outline = self.board_color, dash = self.dash_cond, width=3) 
