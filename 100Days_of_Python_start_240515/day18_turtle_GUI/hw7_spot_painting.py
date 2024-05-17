import turtle as t
import random as rd

# import colorgram
#
# reference_color = colorgram.extract('spot_painting.jpg',15)
#
# colors = []
# for color in reference_color:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors.append((r,g,b))

colors = [(229, 228, 226), (225, 223, 225), (199, 175, 117), (212, 222, 215), (125, 36, 24), (223, 224, 228),
          (167, 106, 56), (186, 159, 52), (6, 57, 83), (108, 68, 85), (112, 161, 175), (21, 122, 174), (63, 153, 138),
          (39, 36, 35), (76, 40, 48)]
t.colormode(255)
t.up()
t.hideturtle()
t.speed("fastest")

x_init = -225
y_init = -225

for i in range(10):
    for j in range(10):
        t.goto(x_init + 50 * j, y_init + 50 * i)
        t.dot(20, rd.choice(colors))

t.exitonclick()
