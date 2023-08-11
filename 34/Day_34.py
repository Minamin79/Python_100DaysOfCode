from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import ui


question_bank = []

for q in question_data:
    question_bank.append(Question(q['text'], q['answer']))
    
quiz = QuizBrain(question_bank)
quiz_ui = ui.QuizInterface(quiz)