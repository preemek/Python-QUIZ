import tkinter as tk
from tkinter import ttk
from Quiz import Questions

class QuizGUI:
    def __init__ (self,root:tk.Tk):
        self.Quiz=Questions()
        self.root=root
        self.root.geometry("400x500")
        self.main_menu()

    def main_menu(self):
        ttk.Label(self.root,text="Welcome to Quiz",anchor="center").pack(side="top",fill="both",expand=True)
        ttk.Button(text="start",command=self.quiz_game).pack(side="top",fill="x",expand=True,padx=100,pady=50)

    def quiz_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        def next_question():
            def show_answer (answer):
                if self.Quiz.check_answer(answer):
                    question_label.config(text="correct!")
                else:
                    question_label.config(text="Wrong, correct answer: {}".format(self.Quiz.get_correct_answer()))
                
                for widget in self.root.winfo_children():
                    if type(widget) is ttk.Button:
                        widget.destroy()
                
                self.Quiz.next_question()
                ttk.Button(self.root,text="next",command=next_question).pack(side="bottom",pady=20,fill="x",expand=True,padx=30)

            for widget in self.root.winfo_children():
                if type(widget) is ttk.Button:
                    widget.destroy()
            question=self.Quiz.get_next_question()
            if question is None:
                self.end_screen()
                return 0

            question_label.config(text=question["Question"])
            for answers in question["Answers"]:
                ttk.Button(text=answers,command=lambda arg=answers:show_answer(arg)).pack(side="left",fill="x",expand=True,padx=10)

        question_label=ttk.Label(self.root,text="")
        question_label.pack(side="top",pady=20)
        next_question()


    def end_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        ttk.Label(self.root,text=f"You have scored {self.Quiz.get_score()}",anchor="center").pack(side="top",fill="both",expand=True)
        ttk.Button(text="close",command=self.root.destroy).pack(side="top",fill="x",expand=True,padx=100,pady=50)

