from ConditionFigure import Figure

class LineStar(Figure):

    def get_star(self, type_line=None, border_color=None):

        self.dash_cond = self.dash_cond if type_line == None else ((10, 2) if type_line == True else None)
        self.board_color = self.board_color if border_color == None else border_color
        
        self.root.create_line(560, 510, 530, 570, fill='white', width=3)
        self.root.create_line(530, 570, 590, 540, fill='white', width=3)
        self.root.create_line(590, 540, 520, 540, fill='white', width=3)
        self.root.create_line(520, 540, 570, 570, fill='white', width=3)
        self.root.create_line(570, 570, 560, 510, fill='white', width=3)

        self.root.create_line(560, 510, 530, 570, dash=self.dash_cond, fill=self.board_color, width=3)
        self.root.create_line(530, 570, 590, 540, dash=self.dash_cond, fill=self.board_color, width=3)
        self.root.create_line(590, 540, 520, 540, dash=self.dash_cond, fill=self.board_color, width=3)
        self.root.create_line(520, 540, 570, 570, dash=self.dash_cond, fill=self.board_color, width=3)
        self.root.create_line(570, 570, 560, 510, dash=self.dash_cond, fill=self.board_color, width=3)
