import turtle as t

X_POS = -240
Y_POS = 230

ALIGN_SCORE = 'left'
ALIGN_OVER = 'center'
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
        self.write(f"SCORE : {self.score}",align=ALIGN_SCORE, font=FONT)

    def upsocre(self):
        self.score += 1
        self.rewrite()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGN_OVER, font=FONT)

