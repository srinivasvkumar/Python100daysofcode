class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list


    def next_question(self):
        curr_quest=self.question_list[self.question_number]
        self.question_number+=1
        ans=input(f"Q.{self.question_number}: {curr_quest.text} (True/False):")

