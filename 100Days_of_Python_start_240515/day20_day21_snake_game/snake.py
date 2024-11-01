from turtle import Turtle

start_len = 3
move_distance = 20
unit_size = 20
start_x = 0
start_y = 0

up = 90
down = 270
right = 0
left = 180


class Snake():
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for idx in range(start_len):
            pos = (start_x - unit_size * idx, start_y)
            self.add_unit(pos)

    def restart(self):
        for unit in self.body:
            unit.hideturtle()
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def add_unit(self, pos):
        tim = Turtle('square')
        tim.color('white')
        # tim.speed(6) # normal speed || range 0.5 ~ 10
        tim.penup()
        tim.goto(pos)
        self.body.append(tim)

    def grow(self):
        self.add_unit(self.body[-1].pos())

    def follow(self):
        # 이전 unit 따라가기
        for idx in range(1, len(self.body)):
            self.body[-idx].goto(self.body[-idx - 1].pos())

    def move(self):
        # 앞으로 전진
        self.follow()
        self.head.fd(move_distance)

    def sethead(self, angle):
        self.head.setheading(angle)


    def up(self):
        if self.head.heading() != down:
            self.sethead(up)
    def down(self):
        if self.head.heading() != up:
            self.sethead(down)

    def right(self):
        if self.head.heading() != left:
            self.sethead(right)
    def left(self):
        if self.head.heading() != right:
            self.sethead(left)