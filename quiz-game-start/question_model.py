# ----------------------------------------
# Question Class
# Represents a single quiz question
# ----------------------------------------

class Question:

    # Initializes a Question object with its text and answer
    def __init__(self, q_text, q_answer):
        self.text = q_text      # Stores the question
        self.answer = q_answer  # Stores the correct answer