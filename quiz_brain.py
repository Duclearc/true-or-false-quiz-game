from question_model import Question


class QuizBrain:
    def __init__(self, questions_list):
        self.question_number: int = 0
        self.questions_list: list = questions_list
        self.current_question: Question = None
        self.game_on: bool = True

    def next_question(self) -> str:
        """returns the current question string."""
        self.current_question = self.questions_list[self.question_number]
        question_header = f'{self.question_number + 1} / {len(self.questions_list)}: True or False?\n\n'
        return f'{question_header}{self.current_question.text}'

    def check_answer(self, given_answer: str) -> bool:
        """takes the user's answer and returns True if it matches the correct answer."""
        if given_answer.title() == self.current_question.answer:
            self.question_number += 1
            return True
        else:
            return False

    def remain_questions(self) -> bool:
        """returns True if there are still unanswered questions."""
        return self.question_number < len(self.questions_list) and self.game_on

    def reset_game(self):
        """resets the question_number and the game_on variable to start a new game."""
        self.question_number = 0
        self.game_on = True
