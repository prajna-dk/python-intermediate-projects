# ----------------------------------------------------------
# Ball Class
# ----------------------------------------------------------
# Controls ball movement, wall collisions, paddle
# collisions, speed changes, and ball reset after scoring.
# ----------------------------------------------------------

from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()

        # Configure the ball
        self.shape("circle")
        self.color("white")
        self.penup()

        # Ball movement variables
        self.next_pos_x = 3
        self.next_pos_y = 3
        self.move_speed = 0.03

    def move(self):
        """Move the ball across the screen."""
        new_x = self.xcor() + self.next_pos_x
        new_y = self.ycor() + self.next_pos_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse the vertical direction."""
        self.next_pos_y *= -1

    def bounce_x(self):
        """Reverse the horizontal direction and increase speed."""
        self.next_pos_x *= -1
        self.move_speed *= 0.9

    def refresh(self):
        """Reset the ball after a player scores."""
        self.goto(0, 0)
        self.move_speed = 0.03
        self.next_pos_x *= -1
        self.next_pos_y *= -1