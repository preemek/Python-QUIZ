import json
import random

class Quiz:
    def __init__(self, filename):
        self.questions = self.load_questions(filename)
        self.score = 0
        self.current_question_index = 0
        random.shuffle(self.questions)

    def load_questions(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    def get_question(self):
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        return None
    def check_answer(self, answer):
        correct = self.questions[self.current_question_index]["answer"]
        if answer == correct:
            self.score += 1
            return True
        return False
    def next_question(self):
        self.current_question_index += 1
        return self.get_question()
    
    def get_score(self):
        return f"Twój wynik to {self.score}/{len(self.questions)}"
    