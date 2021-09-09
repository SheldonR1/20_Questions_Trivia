from question_model import Question
from data import question_data
from quiz_brain import quizManager
questions_bank=[]
for q in question_data:
     q_text=q["question"]
     q_answer=q["correct_answer"]
     new_question=Question(q_text,q_answer)
     questions_bank.append(new_question)

thisQuiz=quizManager(questions_bank)

while thisQuiz.stillHasQuestions():
     thisQuiz.nextQuestion()

print("You've completed the quiz")
print(f"Your final score was: {thisQuiz.score}/{thisQuiz.question_number}")