# import another_module
#
# print(another_module.another_variable)
#
# import turtle

# timmy = turtle.Turtle()

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('brown')
# timmy.forward(50 )
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column(fieldname="Pokemon Name",column=['Pikachu', 'Squirtle', 'Charmander'])
table.add_column(fieldname="Type",column=['Electric', 'Water', 'Fire'])
print(table.align)
table.align = "l"

print(table)


