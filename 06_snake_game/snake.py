# ----------------------------------------------------------
# Snake Class
# ----------------------------------------------------------
# Responsible for creating the snake, moving it, extending
# its body after eating food, and handling direction changes.
# ----------------------------------------------------------

from turtle import Turtle, Screen

# Initial game constants
INITIAL_TAIL_OBJECTS = 3
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
FORWARD_SPACES = 20


class Snake:

    def __init__(self):
        # Store all snake body segments
        self.segments = []

        # Create the initial snake
        self.create_snake_body()

        # Reference to the snake's head
        self.head = self.segments[0]

    def add_segment(self, position):
        """Create and add a new snake segment."""
        segment = Turtle(shape="square")
        segment.penup()
        segment.setposition(position)
        segment.color("White")
        self.segments.append(segment)

    def create_snake_body(self):
        """Build the snake using predefined starting positions."""
        for position in POSITIONS:
            self.add_segment(position)

    def extend(self):
        """Add a new segment to the snake's tail."""
        self.add_segment(self.segments[-1].position())

    def keep_moving_forward(self):
        """Move the snake forward by shifting each segment."""
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].setposition(new_x, new_y)

        self.head.forward(FORWARD_SPACES)

    def up(self):
        """Move the snake upward."""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """Move the snake downward."""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        """Move the snake left."""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """Move the snake right."""
        if self.head.heading() != 180:
            self.head.setheading(0)
