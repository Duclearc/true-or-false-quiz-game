from question_model import Question

RESET = 0


class QuizBrain:
    def __init__(self, questions_list):
        self.question_number: int = RESET
        self.questions_list: list = questions_list
        self.current_question: Question = None
        self.game_on: bool = True

    def next_question(self) -> str:
        self.current_question = self.questions_list[self.question_number]
        question_header = f'{self.question_number + 1}/{len(self.questions_list)} - True or False?\n\n'
        return f'{question_header}{self.current_question.text}'

    def check_answer(self, given_answer: str) -> bool:
        if given_answer.title() == self.current_question.answer:
            self.question_number += 1
            return True
        else:
            return False

    def remain_questions(self) -> bool:
        return self.question_number < len(self.questions_list) and self.game_on

    def reset_game(self):
        self.question_number = RESET
        self.game_on = True
