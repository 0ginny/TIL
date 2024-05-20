import turtle as t

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')
        self.shape('circle')