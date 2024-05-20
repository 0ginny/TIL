from turtle import Screen
from timmy import Timmy
from car import Cars
from scoreboard import ScoreBoard
import time

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

WINING_POS = 250
START_POS = -230

GAME_ON = True
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
    scoreboard = ScoreBoard()

    # turtle control event handler
    screen.listen()
    screen.onkeypress(fun=timmy.up,key='Up')
    screen.onkeypress(fun=timmy.down,key='Down')

    # main loop
    while GAME_ON :
        screen.update()
        time.sleep(cars.car_speed)
        cars.move_cars()

        # set clear
        if timmy.ycor() > WINING_POS:
            timmy.goto(0, START_POS)
            cars.upspeed()
            scoreboard.upsocre()

        # game over
        if cars.car_accident(timmy):
            print('game over!')
            scoreboard.game_over()
            GAME_ON = False

    screen.exitonclick()