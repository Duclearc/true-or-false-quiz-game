class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list

    def next_question(self):
        # check if quiz has ended
        continue_quiz = True
        while self.question_number < len(self.questions_list) and continue_quiz:
            if 0 < self.question_number:
                print(f'CORRECT! You now have {self.question_number} points.')
            current_question = self.questions_list[self.question_number]
            # ask questions and check if answer is correct
            if input(f'True or False? {current_question.text}\n').title() == current_question.answer:
                self.question_number += 1
            else:
                if input("OPS! Sorry, that was incorrect. Play again? Type 'Yes' or 'No'.\n").title() == 'Yes':
                    self.question_number = 0
                    self.next_question()
                else:
                    print('Goodbye! 👋')
                    continue_quiz = False
        if continue_quiz:
            print('CONGRATULATIONS! You won this quiz! 🥳')
            self.question_number = 0
            continue_quiz = False
