from turtle import Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)     # Refresh screen every 0.1 seconds

    snake.move()


screen.exitonclick()
