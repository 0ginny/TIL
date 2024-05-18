from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move():
    tim.fd(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def back_move():
    tim.back(10)

def clear():
    screen.reset()

screen.listen()

screen.onkey(key = 'c', fun = clear)
screen.onkey(key = 'w', fun = move)
screen.onkey(key = 's', fun = back_move)
screen.onkey(key = 'a', fun = turn_left)
screen.onkey(key = 'd', fun = turn_right)



screen.exitonclick()