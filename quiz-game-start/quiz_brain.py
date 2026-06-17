# ----------------------------------------
# QuizBrain Class
# Controls the quiz flow, scoring,
# and answer validation
# ----------------------------------------

class QuizBrain:

    # Initializes the quiz
    def __init__(self, q_list):
        self.question_number = 0      # Tracks the current question number
        self.score = 0                # Stores the user's score
        self.question_list = q_list   # Stores all quiz questions

    # Checks whether there are more questions remaining
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Displays the next question
    def next_question(self):

        # Get the current question
        current = self.question_list[self.question_number]

        # Move to the next question
        self.question_number += 1

        # Ask the user for their answer
        user_answer = input(
            f"Q{self.question_number}: {current.text} (True/False): "
        )

        # Check whether the answer is correct
        self.check_answer(current.answer, user_answer)

    # Validates the user's answer
    def check_answer(self, correct_answer, user_answer):

        # Convert the user's answer to lowercase
        user_answer = user_answer.lower()

        # Accept both the full answer (True/False)
        # and the first letter (T/F)
        if (
            user_answer == correct_answer.lower()
            or user_answer == correct_answer.lower()[0]
        ):
            print("Your answer is correct!")
            self.score += 1
        else:
            print("Incorrect answer.")

        # Show the correct answer
        print(f"The correct answer is {correct_answer}")

        # Display the current score
        print(f"Your current score is {self.score}/{self.question_number}")

        # Print a blank line for readability
        print()