from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def setup_race():
    y_axis = -100
    for color in colors:
        turtle = Turtle(shape='turtle')
        turtle.color(color)
        turtle.penup()
        turtle.goto(x=-230, y=y_axis)
        y_axis += 40
        turtles.append(turtle)

def start_race():
    is_race_on = True

    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


setup_race()
start_race()




screen.exitonclick()