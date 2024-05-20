import turtle as t

START_X = 0
START_Y = -230
START_HEADING = 90
class Timmy(t.Turtle):
    def __init__(self):
        super().__init__()

        self.shape('turtle')
        self.penup()
        self.setheading(START_HEADING)
        self.goto(START_X,START_Y)
