from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.showscore()

    def showscore(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))  
    
    def gameover(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=("Arial", 16, "normal"))