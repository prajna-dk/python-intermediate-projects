# ----------------------------------------------------------
# Turtle Racing Game
# ----------------------------------------------------------
# A simple racing game built using Python's Turtle graphics.
# The user predicts which colored turtle will win the race,
# and each turtle moves forward by a random distance until
# one reaches the finish line.
# ----------------------------------------------------------

from turtle import Turtle, Screen
import random

# Create the game window
screen = Screen()
screen.setup(width=500, height=400)

# Ask the user to predict the winning turtle
user_input = screen.textinput(
    "Hi there!",
    "Which colored turtle will win?\n"
    "'Violet', 'Indigo', 'Blue', 'Green', "
    "'Yellow', 'Orange', or 'Red'"
)

# Available turtle colors
colors = [
    "Violet",
    "Indigo",
    "Blue",
    "Green",
    "Yellow",
    "Orange",
    "Red"
]

# Starting y-coordinate for each turtle
y_positions = [150, 100, 50, 0, -50, -100, -150]

# Store all turtle objects
turtles = []

# Create seven turtles and position them at the starting line
for i in range(7):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=-240, y=y_positions[i])
    turtles.append(turtle)

# Flag to control the race loop
game_over = False

# Continue racing until a turtle reaches the finish line
while not game_over:

    # Move every turtle one after another
    for turtle in turtles:

        # Check if the turtle has crossed the finish line
        if turtle.xcor() >= 230:
            game_over = True

            # Compare user's prediction with the winner
            if user_input.lower() == turtle.pencolor().lower():
                print("🎉 You win!")
            else:
                print("❌ You lose!")
                print(f"{turtle.pencolor()} turtle won!")

        else:
            # Move the turtle forward by a random distance
            turtle.forward(random.randint(1, 10))

# Keep the game window open until clicked
screen.exitonclick()