from ExtendConditionFigure import extendFigure

class Sec(extendFigure):

    def get_sector(self, type_line=None, border_color=None, fill=None):

        self.board_color = self.board_color if border_color == None else border_color
        self.dash_cond = self.dash_cond if type_line == None else ((10, 2) if type_line == True else None)
        self.fill = self.fill if fill == None else fill
            
        self.root.create_arc(153, 426, 453, 726, start=0, extent=64, fill='white', width=2)
        self.root.create_arc(153, 426, 453, 726, start=0, extent=64, fill = self.fill, outline = self.board_color, dash = self.dash_cond, width=2)
