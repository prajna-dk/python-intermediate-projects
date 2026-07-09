from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.shapesize(0.5,0.5)
        self.new_food()
    def new_food(self):
        next_x = random.randint(-280,280)
        next_y = random.randint(-280,280)
        self.setposition(next_x,next_y)
