import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WALL_X = 380
WALL_Y = 280

DISTANCE_MAX = 58
DISTNACE_MIN = 20

TIME_DELAY = 0.02

# main code
if __name__ == '__main__':
    screen = t.Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Pong Game")
    screen.bgcolor('black')

    screen.tracer(0)

    player1 = Paddle()
    player2 = Paddle(player1=False)

    ball = Ball()

    scoreboard = ScoreBoard()

    screen.listen()
    screen.onkey(fun=player1.up, key='w')
    screen.onkey(fun=player1.down, key='s')

    screen.onkey(fun=player2.up, key='Up')
    screen.onkey(fun=player2.down, key='Down')

    while 1:
        screen.update()
        time.sleep(TIME_DELAY)

        # if paddle detact ball
        if player1.distance(ball) <= DISTANCE_MAX and ball.xcor() <= player1.xcor() + DISTNACE_MIN:
            ball.switch_angle_vertical()

        if player2.distance(ball) <= DISTANCE_MAX and ball.xcor() >= player2.xcor() - DISTNACE_MIN:
            ball.switch_angle_vertical()

        if not -WALL_Y <= ball.ycor() <= WALL_Y:
            ball.switch_angle_horizon()

        if not -WALL_X <= ball.xcor() <= WALL_X:
            if ball.xcor() > WALL_X:
                ball.restart(1)
                scoreboard.upscore(1)
            else:
                ball.restart(2)
                scoreboard.upscore(2)

            ball.move_distance = 10

        ball.move()
        ball.move_distance += 0.01

    screen.exitonclick()
