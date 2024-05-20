import turtle as t

STRETCH_WIDTH = 1
STRETCH_HEIGHT = 5

INIT_X = -380
INIT_Y = 0


class Paddle(t.Turtle):
    def __init__(self,player1 = True):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=STRETCH_HEIGHT, stretch_len=STRETCH_WIDTH)
        self.penup()
        if player1:
            self.goto(INIT_X, INIT_Y)
        else :
            self.goto(-INIT_X, INIT_Y)


    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
