import turtle as t
import random

num_circle = 100
t.speed('fastest')
t.colormode(255)
for i in range(num_circle):
    t.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.circle(100)
    t.setheading(i * 360 / num_circle)

t.Screen().exitonclick()