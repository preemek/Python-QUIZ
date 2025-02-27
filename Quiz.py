import json
from random import shuffle


class Questions:
    def __init__(self):
        with open("Python-QUIZ\questions.json", "r") as data:
            self.Question_list=json.load(data)
        shuffle(self.Question_list)
        for question in self.Question_list:
            shuffle(question["Answers"])

        self.Points=0
        self.Index=0
    def next_question(self):
        self.Index+=1
    def check_answer(self,answer:str) -> bool:
        """return True if answer is correct"""
        try:
            if answer==self.Question_list[self.Index]["Correct_Answer"]:
                self.Points+=1
                return True
            else:
                return False
        except Exception as err:
            print(err)
    def get_correct_answer(self):
        return self.Question_list[self.Index]["Correct_Answer"]
    def get_score(self):
        return f"{self.Points}/{len(self.Question_list)}"
    
    def get_correct_answer(self):
        try:
            return self.Question_list[self.Index]["Correct_Answer"]
        except Exception as err:
            print(err)

    def get_next_question(self):
        if self.Index == len(self.Question_list):
            return None
        return {"Question":self.Question_list[self.Index]["Question"],"Answers":self.Question_list[self.Index]["Answers"]}
    
    def save_list_to_json (self):
        with open("Python-QUIZ\questions.json", "w") as outfile:
            json.dump(self.Question_list, outfile)





# a=Questions()

# a.Question_list.append({"Question":"What do i like","Answers":["chockolate","ice cream","smoothies","wafels"],"Correct_Answer":"ice cream"})
# a.Question_list.append({"Question":"What does she like","Answers":["chockolate","ice cream","smoothies","wafels"],"Correct_Answer":"ice cream"})

# a.save_list_to_json()