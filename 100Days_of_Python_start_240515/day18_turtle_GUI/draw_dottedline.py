import turtle as T

pointer = T.Turtle()
screen = T.Screen()
pointer.begin_poly()
pointer.fd(100)
pointer.end_poly()
pointer.fd(100)

screen.exitonclick()