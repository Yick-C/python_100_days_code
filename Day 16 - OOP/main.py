# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
#
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)