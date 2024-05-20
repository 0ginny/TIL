from turtle import Screen
from timmy import Timmy
import time

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# main code
if __name__ == '__main__':
    # create basic screen
    screen = Screen()
    screen.title("Timmy Crossing Game")
    screen.setup(width=SCREEN_WIDTH, height= SCREEN_HEIGHT)

    # create turtle object
    timmy = Timmy()

    # turtle control event handler
    screen.listen()
    screen.onkeypress(fun=timmy.up,key='Up')
    screen.onkeypress(fun=timmy.down,key='Down')



    screen.exitonclick()