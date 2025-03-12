from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
score= ScoreBoard()
food = Food()
snake = Snake()
screen=Screen()


screen.bgcolor("black")
screen.title("Snake game")
screen.setup(width=600, height=600)
screen.tracer(0)
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

    if snake.snakebody[0].distance(food)<15:
        score.score+=1
        score.showscore()
        snake.extendsnake()
        food.move()
        
    if snake.snakebody[0].xcor() >280 or snake.snakebody[0].xcor() < -280 or snake.snakebody[0].ycor() >280 or snake.snakebody[0].ycor() < -280:
        score.gameover()
        game_is_on = False
    for part in snake.snakebody[1::]:
        if snake.snakebody[0].distance(part)<10:
            score.gameover()
            game_is_on= False


screen.exitonclick()