from turtle import Screen, Turtle

pointer = Turtle()
my_screen  = Screen()


pointer.shape('turtle')
for _ in range(4):
    pointer.forward(50)
    pointer.right(90)


my_screen.exitonclick()
