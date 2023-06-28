from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0",
                                 font=(FONT_NAME, 10, "normal"),
                                 background=THEME_COLOR,
                                 foreground="white")
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Placeholder text",
                                                     font=(FONT_NAME, 20, "italic"), width=280)
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image, bg=THEME_COLOR, activebackground=THEME_COLOR,
                                  highlightthickness=0, bd=0, command=lambda: self.compare_answers("True"))
        self.false_button = Button(image=self.false_image, bg=THEME_COLOR, activebackground=THEME_COLOR,
                                   highlightthickness=0, bd=0, command=lambda: self.compare_answers("False"))
        self.add_elements()
        self.window.mainloop()

    def add_elements(self):
        self.get_new_question()
        self.score_label.grid(column=1, row=0, sticky="EW")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def buttons_state(self, state: str):
        self.true_button.config(state=state)
        self.false_button.config(state=state)

    def get_new_question(self):
        self.buttons_state(ACTIVE)
        self.canvas.config(background="white")
        self.update_score()
        if self.quiz.still_has_questions():
            new_question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=new_question_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You finished! Your total score was {self.quiz.score}/10.")
            self.buttons_state(DISABLED)

    def compare_answers(self, user_answer: str):
        self.buttons_state(DISABLED)
        is_answer_correct = self.quiz.check_answer(user_answer=user_answer)
        if is_answer_correct:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_new_question)
