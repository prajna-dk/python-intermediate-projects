# ----------------------------------------------------------
# Food Class
# ----------------------------------------------------------
# Creates the food object and randomly places it within the
# game area whenever the snake eats it.
# ----------------------------------------------------------

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()

        # Configure the food appearance
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.shapesize(0.5, 0.5)

        # Place food at a random location
        self.new_food()

    def new_food(self):
        """Move the food to a random position."""
        next_x = random.randint(-280, 280)
        next_y = random.randint(-280, 280)
        self.setposition(next_x, next_y)
