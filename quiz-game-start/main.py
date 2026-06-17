# Import the Question class
from question_model import Question

# Import the quiz data
from data import question_data

# Import the QuizBrain class
from quiz_brain import QuizBrain


# Stores all Question objects
question_bank = []

# Convert every dictionary into a Question object
for question in question_data:

    new_question = Question(
        question["question"],
        question["correct_answer"]
    )

    question_bank.append(new_question)


# Create a QuizBrain object
quiz = QuizBrain(question_bank)

# Continue asking questions until the quiz ends
while quiz.still_has_questions():
    quiz.next_question()

# Quiz completed
print("Your quiz is now complete!")

# Display the final score
print(f"Your final score is {quiz.score}/{quiz.question_number}")