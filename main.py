from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUI
from html import unescape


question_bank = []
for question in question_data:
    question_bank.append(Question(unescape(question['question']), question['correct_answer']))

game = QuizBrain(question_bank)
quiz_ui = QuizUI()

game.next_question()
