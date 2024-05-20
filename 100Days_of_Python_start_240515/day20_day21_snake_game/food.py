from turtle import Turtle
import random as rd


stretch =.5

max_h = 280
min_h = -280
max_w = 280
min_w = -280


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len= stretch, stretch_wid= stretch)
        self.color('blue')
        self.speed('fastest')
        self.penup()
        self.refresh()

    def refresh(self):
        self.goto(rd.randint(min_w,max_w), rd.randint(min_h,max_h))

