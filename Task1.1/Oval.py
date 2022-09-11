from ExtendConditionFigure import extendFigure

class oval(extendFigure):

    def get_oval(self, type_line=None, border_color=None, fill=None):

        self.board_color = self.board_color if border_color == None else border_color
        self.dash_cond = self.dash_cond if type_line == None else ((10, 2) if type_line == True else None)
        self.fill = self.fill if fill == None else fill
        
        self.root.create_oval(586, 133, 818, 215, fill='white', outline='white', width=2)
        self.root.create_oval(586, 133, 818, 215, fill = self.fill, dash = self.dash_cond, outline = self.board_color, width=2)
