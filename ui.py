from tkinter import *
from quiz_brain import QuizBrain

# CONSTANTS
THEME_COLOR = "#375362"
WIDTH = 300
HEIGHT = 250
PADDING = 20
FONT_SIZE = 20
SCORE_FONT = ('Courier', FONT_SIZE, 'normal')
QUESTION_FONT = ('Arial', FONT_SIZE, 'italic')


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.game = QuizBrain
        self.window = Tk()
        self.window.title('quiz game'.title())
        self.window.config(bg=THEME_COLOR, padx=PADDING, pady=PADDING)

        # SCOREBOARD
        self.scoreboard = Label(text=f"Score: 0", bg=THEME_COLOR, fg='white', font=SCORE_FONT)
        self.scoreboard.grid(row=0, column=1)

        # QUESTIONS
        self.question_board = Canvas(width=WIDTH, height=HEIGHT)
        self.question_text = self.question_board.create_text(
            WIDTH / 2,
            HEIGHT / 2,
            width=WIDTH - PADDING,
            text='lorem ipsum dolor',
            font=QUESTION_FONT
        )
        self.question_board.grid(row=1, column=0, columnspan=2, pady=PADDING)

        # BUTTONS
        true_btn_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_btn_img)
        self.true_button.grid(row=2, column=0)
        false_btn_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_btn_img)
        self.false_button.grid(row=2, column=1)

        self.play_game()
        # KEEP WINDOW OPEN
        self.window.mainloop()

    def play_game(self):
        question_text = self.game.next_question()
