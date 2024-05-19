from turtle import Turtle, Screen
import time
from snake import Snake

go_on = True


# main code
if __name__ == '__main__':
    # create screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake Game')

    screen.tracer(0)  # 화면 전환시 update 해줘야 함.

    snake = Snake()

    while go_on:
        screen.update()
        time.sleep(0.3)
        snake.forward()
    screen.exitonclick()
