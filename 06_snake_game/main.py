# ----------------------------------------------------------
# Snake Game
# ----------------------------------------------------------
# Main program that initializes the game window, creates all
# game objects, handles keyboard input, updates the game
# loop, checks collisions, and controls game flow.
# ----------------------------------------------------------

from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

# Create and configure the game window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

# Create game objects
snake = Snake()
food = Food()
score = Score()

# Listen for keyboard input
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Move the snake forward
    snake.keep_moving_forward()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        score.increase_score()
        snake.extend()

    # Detect collision with the game boundaries
    if (
        snake.head.xcor() >= 300
        or snake.head.xcor() <= -300
        or snake.head.ycor() >= 300
        or snake.head.ycor() <= -300
    ):
        game_is_on = False
        score.on_game_over()

    # Detect collision with the snake's own body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <= 10:
            game_is_on = False

# Keep the window open until clicked
screen.exitonclick()
