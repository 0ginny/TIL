from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

go_on = True
wall_max = 280

# main code
if __name__ == '__main__':
    # create screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake Game')

    screen.tracer(0)  # 화면 전환시 update 해줘야 함.

    snake = Snake()
    food = Food()
    screen.listen()
    score = ScoreBoard()
    screen.onkey(fun=snake.up, key='Up')
    screen.onkey(fun=snake.down, key='Down')
    screen.onkey(fun=snake.right, key='Right')
    screen.onkey(fun=snake.left, key='Left')

    while go_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) <= 15:
            print('nam nam')
            score.upscore()
            food.refresh()

        # 벽에 닿았는지 감지
        if snake.head.xcor() > wall_max or snake.head.xcor() < -wall_max or snake.head.ycor() > wall_max or snake.head.ycor() < -wall_max:
            go_on = False
            score.gameover()

    screen.exitonclick()
