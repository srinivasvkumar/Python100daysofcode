class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        curr_quest = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {curr_quest.text} (True/False):")
        self.check_answer(ans, curr_quest.answer)

    def check_answer(self, ans, curr_ans):
        if ans.lower() == curr_ans.lower():
            self.score += 1
            print("You got it right")
        else:
            print("you got it wrong")
        print(f"correct answer: {curr_ans}")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n")
