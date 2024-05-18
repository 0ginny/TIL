from turtle import Turtle, Screen
import turtle
import random as rd
color_names = ['yellow', "gold", 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue',
               'cyan', 'turquoise',
               "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]

screen = Screen()
screen.setup(500, 400)
#
# bet = turtle.textinput("Make your bet", "who will win the race? Enter a color")


# 단순 반복 작업
def init_turtle(tim, idx ):
    tim.color(color_names[idx])
    tim.shape('turtle')
    tim.up()


start_x = -230
start_y = -180

end = False
class Turtle_new(turtle.Turtle):
    def start(self,idx):
        self.color_name = color_names[idx]
        self.shape('turtle')
        self.color(self.color_name)
        self.penup()
        self.goto(start_x,start_y+ 50 * idx)

    def move(self):
        self.fd(rd.randint(1,21))

    def check_win(self):
        if self.pos()[0] > 190:
            screen.bye()
            print(f'{self.color_name} win!')

#

t1 = Turtle_new()
t2 = Turtle_new()
t3 = Turtle_new()

t1.start(1)
t2.start(2)
t3.start(3)


while 1 :
    t1.move()
    t2.move()
    t3.move()

    t1.check_win()
    t2.check_win()
    t3.check_win()


screen.exitonclick()
