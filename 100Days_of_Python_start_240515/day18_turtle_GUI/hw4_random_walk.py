import turtle as t
import random


t.width(5)
t.speed('fastest')
t.colormode(255)
angles = [0,90,180,270]
for _ in range(200):
    t.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.fd(10)
    t.setheading(random.choice(angles))
t.Screen().exitonclick()