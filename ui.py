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
        """initiates gameplay. Sets background to white.
        If there's unanswered questions left and the user gave a correct answer, loads the next question.
        Else triggers end_of_game."""
        self.question_board.config(bg='white')
        if self.game.remain_questions():
            q_text = self.game.next_question()
            print(self.game.current_question.answer)  # cheat-sheet
            self.question_board.itemconfig(self.question_text, text=q_text)
        else:
            self.end_of_game()

    def end_of_game(self):
        """evaluates if user won or lost and changes screen_text accordingly.
        Sets game_on to False and triggers set_buttons()."""
        if self.game.game_on:
            screen_text = 'CONGRATULATIONS!!! YOU WIN THE GAME!'
        else:
            screen_text = 'Ops. You Lost!'
        self.game.game_on = False
        self.set_buttons()
        self.question_board.itemconfig(self.question_text, text=f'{screen_text}\n\nReplay questions?')

    def answer_true(self):
        """passes 'true' to give_feedback."""
        self.give_feedback('true')

    def answer_false(self):
        """passes 'false' to give_feedback."""
        self.give_feedback('false')

    def give_feedback(self, given_answer):
        """takes the given_answer and checks against the game's current_question.answer.
        If True, changes screen to green and updates the score.
        If False, changes screen to red and sets game_on to False.
        Calls play_game after 1s."""
        if self.game.check_answer(given_answer):
            self.question_board.config(bg='green')
            self.update_score()
        else:
            self.question_board.config(bg='red')
            self.game.game_on = False
        self.window.after(1000, self.play_game)

    def update_score(self):
        """updates the scoreboard Label text attribute to reflect the current game.question_number."""
        self.scoreboard.config(text=f'Score: {self.game.question_number}')

    def continue_true(self):
        """user wishes to replay.
        Resets game, updates_score, resets the button's commands and calls play_game to restart."""
        self.game.reset_game()
        self.update_score()
        self.set_buttons()
        self.play_game()

    def continue_false(self):
        """user wishes to end game.
        Changes screen text accordingly and disables the buttons."""
        self.question_board.itemconfig(self.question_text, text='Goodbye')
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def set_buttons(self):
        """checks value of game_on.
        If True, sets button commands to answer questions.
        Else, sets button commands to continue or end gameplay."""
        if self.game.game_on:
            self.true_button.config(command=self.answer_true)
            self.false_button.config(command=self.answer_false)
        else:
            self.true_button.config(command=self.continue_true)
            self.false_button.config(command=self.continue_false)
