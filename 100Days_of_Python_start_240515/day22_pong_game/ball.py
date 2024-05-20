import turtle as t
import random as rd

Y_MAX = 290
Y_MIN = -290
X_MAX = 390
X_MIN = -390

MOVE_DISTANCE = 10


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')
        self.shape('circle')
        self.penup()
        self.restart()
        self.move_distance = MOVE_DISTANCE
    def move(self):
        self.fd(self.move_distance)

    def switch_angle_vertical(self):
        angle = self.heading()
        new_angle = (360 + 180 - angle) % 360
        self.setheading(new_angle)

    def switch_angle_horizon(self):
        angle = self.heading()
        new_angle = 360 - angle
        self.setheading(new_angle)

    def restart(self, winner = rd.randint(1,2)):
        self.goto(0,0)
        if winner == 2:
            self.setheading(rd.randint(-60,60))
        else :
            self.setheading(rd.randint(120, 240))
