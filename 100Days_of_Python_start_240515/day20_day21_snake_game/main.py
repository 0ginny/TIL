from turtle import Turtle, Screen

snake = []


def init_game():
    start_x = 0
    start_y = 0

    for idx in range(3):
        tim = Turtle('square')
        tim.color('white')
        tim.speed(6) # normal speed || range 0.5 ~ 10
        tim.penup()
        tim.goto(start_x - 20 * idx, start_y)
        snake.append(tim)


# main code
if __name__ == '__main__':
    # create screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake Game')

    init_game()

    screen.exitonclick()
