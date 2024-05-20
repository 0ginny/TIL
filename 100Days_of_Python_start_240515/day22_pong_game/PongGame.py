import turtle as t
from paddle import Paddle
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WALL_X = 380
WALL_Y = 280

# main code
if __name__ == '__main__' :
    screen = t.Screen()
    screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
    screen.title("Pong Game")
    screen.bgcolor('black')

    screen.tracer(0)

    player1 = Paddle()
    player2 = Paddle(player1=False)

    ball = Ball()

    screen.listen()
    screen.onkey(fun=player1.up, key='w')
    screen.onkey(fun=player1.down, key='s')

    screen.onkey(fun=player2.up, key='Up')
    screen.onkey(fun=player2.down, key='Down')

    while 1:
        screen.update()
        time.sleep(0.05)


        # if paddle detact ball
        if player1.distance(ball) <= 55 and ball.xcor() <= player1.xcor()+20:
            ball.switch_angle_vertical()

        if player2.distance(ball) <= 55 and ball.xcor() >= player2.xcor()-20:
            ball.switch_angle_vertical()

        if not -WALL_Y <= ball.ycor() <= WALL_Y :
            ball.switch_angle_horizon()


        ball.move()

    screen.exitonclick()