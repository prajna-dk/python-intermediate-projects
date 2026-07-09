# ----------------------------------------------------------
# Paddle Class
# ----------------------------------------------------------
# Creates player paddles and controls vertical movement
# within the game boundaries.
# ----------------------------------------------------------

from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        # Configure paddle appearance
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(position)

    def move_up(self):
        """Move the paddle upward."""
        if self.ycor() < 250 or self.ycor() <= -250:
            self.forward(20)

    def move_down(self):
        """Move the paddle downward."""
        if self.ycor() >= 250 or self.ycor() > -250:
            self.back(20)