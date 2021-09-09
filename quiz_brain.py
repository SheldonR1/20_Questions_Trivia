class quizManager:

     def __init__(self, q_list) -> None:
         self.question_number = 0
         self.question_list = q_list
         self.score=0
     
     def nextQuestion(self):
          current_question=self.question_list[self.question_number]
          self.question_number+=1
          user_answer=input(f" #{self.question_number}: {current_question.text} (True or False): ")
          self.checkAnswer(user_answer, current_question.answer)

     def stillHasQuestions(self):
          return self.question_number < len(self.question_list)
     
     def checkAnswer(self,user_answer, correct_answer):
          if user_answer.lower()==correct_answer.lower():
               print("        you got it!")
               self.score=+1
          else:
               print("        that's wrong ")
          print(f"the correct answer is {correct_answer}")
          print(f"Your score is {self.score}/{self.question_number}")
     