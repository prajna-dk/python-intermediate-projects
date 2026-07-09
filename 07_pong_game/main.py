# ----------------------------------------------------------
# Pong Game
# ----------------------------------------------------------
# Main program that creates the game window, initializes all
# game objects, handles keyboard input, updates the game
# loop, detects collisions, and manages scoring.
# ----------------------------------------------------------

from turtle import Screen
from Paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create and configure the game window
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create scoreboards
scoreboard_l = Scoreboard((-50, 250))
scoreboard_r = Scoreboard((50, 250))

# Create paddles
paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))

# Create the ball
ball = Ball()

# Listen for keyboard input
screen.listen()
screen.onkeypress(fun=paddle_l.move_up, key="w")
screen.onkeypress(fun=paddle_r.move_up, key="Up")
screen.onkeypress(fun=paddle_l.move_down, key="s")
screen.onkeypress(fun=paddle_r.move_down, key="Down")

game_is_on = True

# Main game loop
while game_is_on:

    screen.update()
    time.sleep(ball.move_speed)

    # Move the ball
    ball.move()

    # Detect collision with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with either paddle
    if (
        ball.distance(paddle_r) < 40 and ball.xcor() > 330
        or ball.distance(paddle_l) < 40 and ball.xcor() < -330
    ):
        ball.bounce_x()

    # Left player scores
    if ball.xcor() > 390:
        ball.refresh()
        scoreboard_l.update_score()

    # Right player scores
    if ball.xcor() < -390:
        ball.refresh()
        scoreboard_r.update_score()

# Keep the game window open
screen.exitonclick()