from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 18, "italic")

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_text = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quiz_text = self.canvas.create_text(
            150, 125,
            text="The question",
            width=280,
            font=QUESTION_FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_pressed, bd=0)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.false_pressed, bd=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white") # Reset canvas colour
        self.score_text.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz!")
            self.buttons_state(DISABLED)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def buttons_state(self, state):
        self.true_btn.config(state=state)
        self.false_btn.config(state=state)


