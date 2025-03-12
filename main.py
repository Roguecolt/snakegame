from turtle import Screen, Turtle
from snake import Snake
import time
screen=Screen()
snake = Snake()

screen.bgcolor("black")
screen.title("Snake game")
screen.setup(width=600, height=600)
screen.tracer(0)
#Creates snakes body
screen.listen()
screen.onkey(key='w', fun=snake.up)
screen.onkey(key='s', fun=snake.down)
screen.onkey(key='a', fun=snake.left)
screen.onkey(key='d', fun=snake.right)


#Move the snake body
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    


screen.exitonclick()