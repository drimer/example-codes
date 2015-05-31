class Line(object):
    
    def __init__(self):
        self.visible = True


class Canvas(object):
    
    def draw(self, figure):
        pass

def draw_figure_on_canvas(figure, canvas):
    if figure.visible:
        canvas.draw(figure)
