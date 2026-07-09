from turtle import Turtle, Screen

INITIAL_TAIL_OBJECTS = 3
POSITIONS = [(0,0),(-20,0),(-40,0)]
FORWARD_SPACES = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake_body()
        self.head = self.segments[0]
    
    def add_segment(self,position):
        tim = Turtle(shape="square")
        tim.penup()
        tim.setposition(position)
        tim.color("White")
        self.segments.append(tim)

    def create_snake_body(self):
        for position in POSITIONS:
            self.add_segment(position)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def keep_moving_forward(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].setposition(new_x,new_y)
        self.head.forward(FORWARD_SPACES)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
