from tkinter import *

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0",
                                 font=(FONT_NAME, 10, "normal"),
                                 background=THEME_COLOR,
                                 foreground="white")
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.create_text(150, 125, text="Placeholder text",
                                font=(FONT_NAME, 20, "italic"))
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image, bg=THEME_COLOR, activebackground=THEME_COLOR,
                                  highlightthickness=0, bd=0)
        self.false_button = Button(image=self.false_image, bg=THEME_COLOR, activebackground=THEME_COLOR,
                                   highlightthickness=0, bd=0)
        self.add_elements()
        self.window.mainloop()

    def add_elements(self):
        self.score_label.grid(column=1, row=0, sticky="EW")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
