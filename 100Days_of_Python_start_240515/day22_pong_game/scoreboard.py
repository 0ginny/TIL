import turtle as t

BOARD_X = 0
BOARD_Y = 200

ALIGN = 'center'

FONT = ('Courier', 60, 'bold')


class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.p1score = 0
        self.p2score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(BOARD_X,BOARD_Y)
        self.rewrite()

    def upscore(self, player):
        if player == 1:
            self.p1score += 1
        elif player == 2:
            self.p2score += 1
        self.rewrite()

    def rewrite(self):
        self.clear()
        self.write(f"{self.p1score} : {self.p2score}", align=ALIGN, font=FONT)
