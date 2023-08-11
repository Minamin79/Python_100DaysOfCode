import html


class QuizBrain:
    def __init__(self, quetion_list):
        self.question_number = 0
        self.quetion_list = quetion_list
        self.score = 0


    def next_question(self):
        self.current_question = self.quetion_list[self.question_number]
        self.question_number += 1
        return f"Q{self.question_number}. {html.unescape(self.current_question.text)}"
        self.check_answer(user_answer, current_question.answer)


    def still_has_question(self):
        if self.question_number < len(self.quetion_list):
            return True
        else:
            return False
        

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False