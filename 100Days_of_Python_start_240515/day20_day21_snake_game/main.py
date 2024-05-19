from turtle import Turtle, Screen
import time

snake = []

go_on = True


def init_game():
    start_x = 0
    start_y = 0

    for idx in range(3):
        tim = Turtle('square')
        tim.color('white')
        # tim.speed(6) # normal speed || range 0.5 ~ 10
        tim.penup()
        tim.goto(start_x - 20 * idx, start_y)
        snake.append(tim)

    screen.update()


def animation_delay(delay):
    screen.tracer(delay)


def snake_move():
    for unit in snake:
        unit.fd(20)

    # 이전 unit 방향 가져오기
    for idx in range(1,len(snake)):
        snake[-idx].setheading(snake[-idx - 1].heading())
    time.sleep(0.3)
    screen.update()

def turn_left():
    snake[0].setheading(snake[0].heading + 90)


def turn_right():
    snake[0].setheading(snake[0].heading - 90)

# main code
if __name__ == '__main__':
    # create screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake Game')

    animation_delay(0)  # 화면 전환시 update 해줘야 함.

    init_game()

    animation_delay(0)
    # while go_on :
    for _ in range(10):
        snake_move()



    for _ in range(10):
        snake_move()

    screen.exitonclick()
