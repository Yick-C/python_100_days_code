from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.stage = 1
        self.goto(-280, 250)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Stage: {self.stage}", align="left", font=FONT)

    def next_stage(self):
        self.stage += 1
        self.update_scoreboard()
