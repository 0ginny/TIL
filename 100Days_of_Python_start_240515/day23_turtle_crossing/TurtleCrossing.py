from turtle import Screen
from timmy import Timmy
from car import Cars
import time

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# main code
if __name__ == '__main__':
    # create basic screen
    screen = Screen()
    screen.title("Timmy Crossing Game")
    screen.setup(width=SCREEN_WIDTH, height= SCREEN_HEIGHT)
    screen.tracer(0)
    # create object
    timmy = Timmy()
    cars = Cars()
    # turtle control event handler
    screen.listen()
    screen.onkeypress(fun=timmy.up,key='Up')
    screen.onkeypress(fun=timmy.down,key='Down')

    while 1 :
        screen.update()
        time.sleep(cars.car_speed)
        cars.move_cars()

    screen.exitonclick()