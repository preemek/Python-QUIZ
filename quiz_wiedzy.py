import tkinter as tk
from tkinter import messagebox
import csv
import random
import time

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Wiedzy")
        self.root.geometry("500x400")

        self.questions = self.load_questions("pytania.csv")
        self.current_question_index = 0
        self.score = 0
        self.time_limit = 10 
        self.timer_id = None

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=450)
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 12), width=30, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.timer_label = tk.Label(root, text="", font=("Arial", 12))
        self.timer_label.pack(pady=10)

        self.next_question()

    def load_questions(self, filename):
        "Load questions from a CSV file."
        questions = []
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                questions.append(row)
        random.shuffle(questions)
        return questions

    def next_question(self):
        "Display the next question."
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["Pytanie"])

            options = [question_data["Odpowiedź A"], question_data["Odpowiedź B"],
                       question_data["Odpowiedź C"], question_data["Odpowiedź D"]]
            for i, button in enumerate(self.option_buttons):
                button.config(text=options[i])

            self.start_timer()
        else:
            self.end_quiz()

    def check_answer(self, selected_option):
        "Check if the selected answer is correct."
        if self.timer_id:
            self.root.after_cancel(self.timer_id) 

        question_data = self.questions[self.current_question_index]
        correct_answer = question_data["Poprawna odpowiedź"]
        selected_answer = chr(65 + selected_option)  

        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Wynik", "Poprawna odpowiedź!")
        else:
            messagebox.showinfo("Wynik", f"Błędna odpowiedź! Poprawna odpowiedź to: {correct_answer}")

        self.current_question_index += 1
        self.next_question()

    def start_timer(self):
        "Start a countdown timer for the current question."
        self.time_left = self.time_limit
        self.update_timer()

    def update_timer(self):
        "Update the timer display."
        self.timer_label.config(text=f"Czas: {self.time_left} sekund")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Czas", "Czas minął!")
            self.current_question_index += 1
            self.next_question()

    def end_quiz(self):
        "End the quiz and display the final score."
        messagebox.showinfo("Koniec quizu", f"Twój wynik to {self.score}/{len(self.questions)}")
        self.save_score(self.score)
        self.root.destroy()

    def save_score(self, score):
        "Save the player's score to a file."
        with open("wyniki.txt", mode="a", encoding="utf-8") as file:
            file.write(f"Wynik: {score}/{len(self.questions)}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()