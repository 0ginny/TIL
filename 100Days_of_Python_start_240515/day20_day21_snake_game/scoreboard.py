import turtle as t

score_x = 0
score_y = 275

ALIGNMENT = 'center'
FONT = ('Arial', 15, 'bold')
# turtle 을 바로 상속할 수 없어. turtle은 module이야.
# class 상속은 class를 해야하고.
class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(score_x, score_y)
        self.score = 0
        self.rewrite()

    def rewrite(self):
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGNMENT, font= FONT)

    def upscore(self):
        self.score += 1
        self.rewrite()
