import turtle as t

X_POS = -240
Y_POS = 230

ALIGN = 'left'
FONT = ('Arial', 10, 'bold')
class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.goto(X_POS,Y_POS)
        self.score = 0
        self.rewrite()

    def rewrite(self):
        self.clear()
        self.write(f"SCORE : {self.score}",align=ALIGN, font=FONT)

    def upsocre(self):
        self.score += 1
        self.rewrite()
