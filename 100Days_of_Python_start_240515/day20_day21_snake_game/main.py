from turtle import Screen
import time
from snake import Snake
from food import Food

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
    food = Food()
    screen.listen()

    screen.onkey(fun = snake.up , key= 'Up')
    screen.onkey(fun = snake.down , key= 'Down')
    screen.onkey(fun = snake.right , key= 'Right')
    screen.onkey(fun = snake.left , key= 'Left')


    while go_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) <= 15:
            print('nam nam')
            food.refresh()

    screen.exitonclick()
