from turtle import Turtle, Screen
import turtle
import random as rd
color_names = ['yellow', "gold", 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue',
               'cyan', 'turquoise',
               "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]

screen = Screen()
screen.setup(500, 500)
#
bet = turtle.textinput("Make your bet", "who will win the race? Enter a color")


start_x = -230
start_y = -200

turtles = []

for idx in range(11):
    tim= Turtle(shape = 'turtle')
    tim.color(color_names[idx])
    tim.penup()
    tim.goto(start_x,start_y + 40 * idx)
    turtles.append(tim)

race_end = False
winner_color = ''

while not race_end :
    rd.shuffle(turtles)
    for turtle in turtles:
        turtle.fd(rd.randint(1,30))

        if turtle.xcor() > 230:
            race_end = True
            winner_color = turtle.pencolor()
if bet == winner_color :
    print(f'You Win! {winner_color} is win!')
else :
    print(f'You loose! {winner_color} is win!')


screen.exitonclick()
