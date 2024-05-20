import turtle as t
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


# main code
if __name__ == '__main__' :
    screen = t.Screen()
    screen.screensize(canvwidth=SCREEN_WIDTH, canvheight=SCREEN_HEIGHT)
    screen.title("Pong Game")
    screen.bgcolor('black')




    screen.exitonclick()