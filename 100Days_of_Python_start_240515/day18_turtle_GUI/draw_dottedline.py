import turtle as T

pointer = T.Turtle()
screen = T.Screen()
for _ in range(15):
    pointer.fd(10)
    pointer.up()
    pointer.fd(10)
    pointer.down()
screen.exitonclick()