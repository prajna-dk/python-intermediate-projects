from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.keep_moving_forward()

    if snake.head.distance(food) < 15:
        food.new_food()
        score.increase_score()
        snake.extend()
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        game_is_on = False
        score.on_game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <= 10:
            game_is_on = False

screen.exitonclick()