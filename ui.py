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
        self.game = quiz_brain
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
        self.true_button = Button(image=true_btn_img, command=self.answer_true)
        self.true_button.grid(row=2, column=0)
        false_btn_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_btn_img, command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        # INITIATE GAMEPLAY
        self.play_game()
        self.window.mainloop()

    def play_game(self):
        self.question_board.config(bg='white')
        if self.game.remain_questions():
            q_text = self.game.next_question()
            print(self.game.current_question.answer)
            self.question_board.itemconfig(self.question_text, text=q_text)
        else:
            if self.game.game_on:
                screen_text = 'CONGRATULATIONS!!! YOU WIN THE GAME!'
            else:
                screen_text = 'Ops. You Lost!'
            self.game.game_on = False
            self.question_board.itemconfig(self.question_text, text=f'{screen_text}\n\nReplay questions?')
            self.set_buttons()

    def answer_true(self):
        self.give_feedback('true')

    def answer_false(self):
        self.give_feedback('false')

    def give_feedback(self, answer):
        if self.game.check_answer(answer):
            self.question_board.config(bg='green')
            self.update_score()
        else:
            self.question_board.config(bg='red')
            self.game.game_on = False
        self.window.after(1000, self.play_game)

    def update_score(self):
        self.scoreboard.config(text=f'Score: {self.game.question_number}')

    def continue_true(self):
        self.game.reset_game()
        self.update_score()
        self.set_buttons()
        self.play_game()

    def continue_false(self):
        self.question_board.itemconfig(
            self.question_text,
            text='Goodbye'
        )
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def set_buttons(self):
        if self.game.game_on:
            self.true_button.config(command=self.answer_true)
            self.false_button.config(command=self.answer_false)
        else:
            self.true_button.config(command=self.continue_true)
            self.false_button.config(command=self.continue_false)
