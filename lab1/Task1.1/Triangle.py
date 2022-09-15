from ExtendConditionFigure import extendFigure

class Trian(extendFigure):

    def get_triangle(self, type_line=None, border_color=None, fill=None):

        self.board_color = self.board_color if border_color == None else border_color
        self.dash_cond = self.dash_cond if type_line == None else ((10, 2) if type_line == True else None)
        self.fill = self.fill if fill == None else fill

        
        self.root.create_polygon(648, 460, 781, 303, 886, 406, fill="white", width=3, outline='white')
        self.root.create_polygon(648, 460, 781, 303, 886, 406, fill = self.fill, outline= self.board_color, dash = self.dash_cond, width=3)
