from tkinter import *
from quiz_brain import QuizBrain
import data


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quiz')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(150, 120, width=280, text='Question', font=('Arial', 15), fill='black')
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        self.score_label = Label(text=f'Score: 0', font=('Arial', 12, 'bold') , fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=1, column=2)

        self.right_img = PhotoImage(file='images/true.png')
        self.right_button = Button(image=self.right_img, command=self.true_pressed, highlightthickness=0)
        self.right_button.grid(row=4, column=2)

        self.false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_img, command=self.false_pressed, highlightthickness=0)
        self.false_button.grid(row=4, column=1)

        self.get_next_question()
        self.window.mainloop()

    
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_question():   
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")
            self.right_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))


    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)