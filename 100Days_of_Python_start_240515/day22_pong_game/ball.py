import turtle as t
import random as rd

Y_MAX = 290
Y_MIN = -290
X_MAX = 390
X_MIN = -390

MOVE_DISTANCE = 20

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')
        self.shape('circle')
        self.penup()
        self.setheading(rd.randint(1,360))

    def move(self):
        self.fd(MOVE_DISTANCE)