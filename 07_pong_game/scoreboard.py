# ----------------------------------------------------------
# Scoreboard Class
# ----------------------------------------------------------
# Tracks each player's score and updates the scoreboard
# whenever a point is scored.
# ----------------------------------------------------------

from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()

        # Configure scoreboard
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)

        # Initialize score
        self.score = 0

        # Display the initial score
        self.write(
            arg=self.score,
            font=("Arial", 20, "normal")
        )

    def update_score(self):
        """Increase and display the player's score."""
        self.score += 1
        self.clear()
        self.write(
            arg=self.score,
            font=("Arial", 20, "normal")
        )