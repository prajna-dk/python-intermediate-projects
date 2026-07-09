# ----------------------------------------------------------
# Score Class
# ----------------------------------------------------------
# Keeps track of the player's score, updates the scoreboard,
# and displays the Game Over message.
# ----------------------------------------------------------

from turtle import Turtle


class Score(Turtle):

    def __init__(self, shape="classic"):
        super().__init__(shape)

        # Configure the scoreboard
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)

        # Display the initial score
        self.update_score()

    def update_score(self):
        """Refresh the displayed score."""
        self.clear()
        self.write(
            arg=f"Score is {self.score}",
            move=False,
            align="center",
            font=("Arial", 18, "normal")
        )

    def increase_score(self):
        """Increase the score after food is collected."""
        self.score += 1
        self.update_score()

    def on_game_over(self):
        """Display the Game Over message."""
        self.goto(0, 0)
        self.write(
            arg="GAME OVER",
            move=False,
            align="center",
            font=("Arial", 20, "normal")
        )
