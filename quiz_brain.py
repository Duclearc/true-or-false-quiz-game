RESET = 0


class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = RESET
        self.questions_list = questions_list
        self.current_question = None
        self.game_on = False

    def next_question(self):
        self.current_question = self.questions_list[self.question_number]
        question_header = f'{self.question_number+1}/{len(self.questions_list)} - True or False?\n'
        return f'{question_header}{self.current_question.text}'

    def offer_replay(self):
        if self.question_number < len(self.questions_list):
            print('OPS! Sorry, that was incorrect.')
        if input("Play again? Type 'Yes' or 'No'.\n").title() == 'Yes':
            self.play_game()
        else:
            print('Goodbye! 👋')
            self.game_on = False

    def show_score(self):
        print(f'CORRECT! You now have {self.question_number} points.')

    def check_answer(self, given_answer):
        self.question_number += 1
        if given_answer.title() == self.current_question.answer:
            self.show_score()
        else:
            self.offer_replay()

    def announce_victory(self):
        if self.game_on:
            print('CONGRATULATIONS! You won this quiz! 🥳')
            self.offer_replay()

    def play_game(self):
        self.question_number = RESET
        self.game_on = True
        while self.question_number < len(self.questions_list) and self.game_on:
            answer = input(f'{self.next_question()} => {self.current_question.answer}\n-> ')
            self.check_answer(answer)
        self.announce_victory()
