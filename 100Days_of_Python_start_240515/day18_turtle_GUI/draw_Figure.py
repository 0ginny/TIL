import turtle as t
import random

def draw_figure(angles):
    t.pencolor((random.randrange(0,256),random.randrange(0,256),random.randrange(0,256)))
    if angles > 2:
        home = -t.position()
        while 1:
            # print(t.position())
            t.forward(100)
            t.right(360/angles)

            if abs(t.pos()) < 1:
                # print("fin")
                break



screen = t.Screen()
p = t.Turtle()

t.width(4)
t.colormode(255)
repeat = 10
for num in range(3,repeat+3):
    draw_figure(num)

screen.exitonclick()