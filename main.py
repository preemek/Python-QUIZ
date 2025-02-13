import tkinter as tk
from quiz import Quiz
from quiz_ui import QuizUI
if __name__ == "__main__":
    quiz = Quiz("questions.json")
    root = tk.Tk()
    app = QuizUI(root, quiz)
    root.mainloop()