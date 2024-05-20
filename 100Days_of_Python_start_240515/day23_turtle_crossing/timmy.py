import turtle as t

START_X = 0
START_Y = -230
START_HEADING = 90
MOVE_DISTANCE = 20
class Timmy(t.Turtle):
    def __init__(self):
        super().__init__()

        self.shape('turtle')
        self.penup()
        self.setheading(START_HEADING)
        self.goto(START_X,START_Y)

    def up(self):
        self.fd(MOVE_DISTANCE)

    def down(self):
        self.back(MOVE_DISTANCE)
