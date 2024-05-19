from turtle import Turtle

start_len = 3
move_distance = 20
unit_size = 20
start_x = 0
start_y = 0


class Snake():
    def __init__(self):
        self.body = []
        self.create_snake()

    def create_snake(self):
        for idx in range(start_len):
            tim = Turtle('square')
            tim.color('white')
            # tim.speed(6) # normal speed || range 0.5 ~ 10
            tim.penup()
            tim.goto(start_x - unit_size * idx, start_y)
            self.body.append(tim)

    def follow(self):
        # 이전 unit 따라가기
        for idx in range(1, len(self.body)):
            self.body[-idx].goto(self.body[-idx - 1].pos())

    def forward(self):
        # 앞으로 전진
        self.follow()
        self.body[0].fd(move_distance)
