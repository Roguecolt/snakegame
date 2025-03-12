from turtle import Turtle
STARTINGPOSITION = [(0, 0), (-20, 0), (-40, 0)]
class Snake:

    def __init__(self):
        self.snakebody = []
        self.xaxis=0
        self.createsnake()
        
        

    def createsnake(self):
        for position in STARTINGPOSITION:
            self.addtosnake(position)
    def addtosnake(self,position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snakebody.append(new_snake)

    def extendsnake(self):
        self.addtosnake(self.snakebody[-1].position())
        
    def move(self):
        for snakepart in range(len(self.snakebody)-1,0,-1):
            new_x = self.snakebody[snakepart-1].xcor()
            new_y = self.snakebody[snakepart-1].ycor()
            self.snakebody[snakepart].goto(x=new_x,y=new_y)
        self.snakebody[0].forward(20)

    def up(self):
        if self.snakebody[0].heading() != 270:
            self.snakebody[0].setheading(90)
        
    def down(self):
        if self.snakebody[0].heading() != 90:
            self.snakebody[0].setheading(270)
        
    def left(self):
        if self.snakebody[0].heading() !=  0:
            self.snakebody[0].setheading(180)
        
    def right(self):
        if self.snakebody[0].heading() != 180:
            self.snakebody[0].setheading(0)
    



# 


# for snakepart in range(len(snakebody)-1,0,-1):
#           new_x = snakebody[snakepart-1].xcor()
#           new_y = snakebody[snakepart-1].ycor()
#           snakebody[snakepart].goto(x=new_x,y=new_y)
#     snakebody[0].forward(20)

