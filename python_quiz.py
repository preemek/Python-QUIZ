import json
import random
import tkinter as tk
from tkinter import messagebox
import time


class Quiz:
    def __init__(self, file, category):
        self.questions = self.load_questions(file, category)
        self.score = 0
        self.current_question = 0
        self.start_time = None
        self.time_limit = 10

    def load_questions(self, file, category):

        with open(file, 'r', encoding='utf-8') as f:
            all_questions = json.load(f)
        category_questions = [q for q in all_questions if q["category"] == category]
        return random.sample(category_questions, len(category_questions))
        
    def check_answer(self, answer):
        correct = self.questions[self.current_question]['correct']
        if answer == correct:
            self.score += 1
        self.current_question += 1

    def is_finished(self):
        return self.current_question >= len(self.questions)
    
    def get_question(self):
        if not self.is_finished():
            return self.questions[self.current_question]
        return None
    
    def save_score(self, name):
        with open("ranking.txt", 'a', encoding='utf-8') as f:
            f.write(f"{name}: {self.score}/{len(self.questions)}\n")


class QuizGUI:
    def __init__(self, root, quiz):
        self.root = root
        self.quiz = quiz
        self.root.title("Quiz Wiedzy")
        self.name = tk.StringVar()
        self.category = tk.StringVar()
        self.create_widgets()
        

    def create_widgets(self):
        self.label_name = tk.Label(self.root, text="Podaj swoje imię")
        self.label_name.pack()
        self.entry_name = tk.Entry(self.root, textvariable=self.name)
        self.entry_name.pack()

        self.label_category = tk.Label(self.root, text="Wybierz kategorię:")
        self.label_category.pack()
        self.category_menu = tk.OptionMenu(self.root, self.category, "Historia", "Nauka", "Sport")
        self.category_menu.pack()

        self.button_start = tk.Button(self.root, text="Start", command=self.start_quiz)
        self.button_start.pack()

        self.question_label = tk.Label(self.root, text="", wraplength=400)
        self.question_label.pack()

        self.buttons = {}
        for option in ['A', 'B', 'C', 'D']:
            self.buttons[option] = tk.Button(self.root, text="", command=lambda opt=option: self.answer(opt))
            self.buttons[option].pack()

        self.timer_label = tk.Label(self.root, text="Czas: 10s")
        self.timer_label.pack()


    def start_quiz(self):
        self.player_name = self.name.get()
        self.selected_category = self.category.get()
        if not self.player_name:
            messagebox.showwarning("Błąd", "Podaj imię!")
            return
        if not self.selected_category:
            messagebox.showwarning("Błąd", "Wybierz kategorię!")
            return
        

        self.quiz = Quiz("pytania.json", self.selected_category)

        self.entry_name.pack_forget()
        self.button_start.pack_forget()
        self.label_name.pack_forget()
        self.label_category.pack_forget()
        self.category_menu.pack_forget()


        self.next_question()

    def next_question(self):
        question = self.quiz.get_question()
        if question:
            self.question_label.config(text=question['question'])
            for opt in ['A', 'B', 'C', 'D']:
                self.buttons[opt].config(text=question['options'][opt])
            self.quiz.start_time = time.time()
            self.update_timer()
        else:
            self.end_quiz()

    def update_timer(self):
        if self.quiz.start_time is None:
            return

        remaining = self.quiz.time_limit - int(time.time() - self.quiz.start_time)
        if remaining > 0:
            self.timer_label.config(text=f"Czas: {remaining}s")
            self.root.after(1000, self.update_timer)
        else:
            self.answer(None)


    def answer(self, answer):
        if answer:
            self.quiz.check_answer(answer)
        self.next_question()

    def end_quiz(self):
        messagebox.showinfo("Koniec gry", f"Twój wynik to {self.quiz.score}/{len(self.quiz.questions)}")
        self.quiz.save_score(self.player_name)
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    
    app = QuizGUI(root, None)
    root.mainloop()





