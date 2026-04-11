import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(800, 550)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_file = pandas.read_csv("50_states.csv")
all_states = states_file.state.to_list()
guessed_states = []

while len(guessed_states) < 50:  # .title() function will format the answer correctly
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":  # Finish game and save remaining states in csv file
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_row = states_file[states_file.state == answer_state]
        t.goto(state_row.x.item(), state_row.y.item())
        t.write(answer_state)

# screen.exitonclick() # Can't use this as we need to click on the screen