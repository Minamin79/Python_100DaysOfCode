class QuizBrain:
    def __init__(self, quetion_list):
        self.question_number = 0
        self.quetion_list = quetion_list
        self.score = 0

    def next_question(self):
        current_question = self.quetion_list[self.question_number]
        user_answer = input(f"Q{self.question_number + 1}. {self.quetion_list[self.question_number].text} (True/False)? ").title()
        while user_answer != 'True' and user_answer != 'False':
            print('Invalid input.')
            user_answer = input(f"Q{self.question_number + 1}. {self.quetion_list[self.question_number].text} (True/False)? ").title()
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        if self.question_number < len(self.quetion_list):
            return True
        else:
            return False
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print('That\'s wrong!')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print('\n')