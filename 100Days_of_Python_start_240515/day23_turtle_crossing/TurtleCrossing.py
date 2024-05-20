from turtle import Screen
from timmy import Timmy
import time

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# main code
if __name__ == '__main__':
    screen = Screen()
    screen.title("Timmy Crossing Game")
    screen.setup(width=SCREEN_WIDTH, height= SCREEN_HEIGHT)

    timmy = Timmy()

    screen.exitonclick()