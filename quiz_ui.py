import tkinter
from tkinter import messagebox
from quiz import Quiz

class QuizUI:
    def __init__(self, root, quiz):
        self.quiz = quiz
        self.root = root
        self.root.title("Quiz Wiedzy")

        self.question_label = tkinter.Label(root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tkinter.Button(root, text="", width=40, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.next_button = tkinter.Button(root, text="Dalej", command=self.next_question)
        self.next_button.pack(pady=20)

        self.next_question()

    def next_question(self):
        self.current_question = self.quiz.next_question()
        if self.current_question:
            self.question_label.config(text=self.current_question["question"])
            options = self.current_question["options"]
            for i in range(4):
                self.buttons[i].config(text=options[i], state=tkinter.NORMAL)
        else:
            messagebox.showinfo("Koniec", self.quiz.get_score())
            self.root.quit()

    def check_answer(self, index):
        selected_option = self.buttons[index]["text"]
        correct = self.quiz.check_answer(selected_option)
        if correct:
            messagebox.showinfo("Odpowiedź", "Poprawna odpowiedź!")
        else:
            messagebox.showinfo("Odpowiedź", "Błędna odpowiedź!")
        for btn in self.buttons:
            btn.config(state=tkinter.DISABLED)
        self.root.after(1000, self.next_question)

    