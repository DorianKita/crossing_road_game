from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-280,250)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.write(arg=f'Level: {self.score}', align='left',font=FONT)


    def change_level(self):
        self.score +=1
        self.clear()
        self.write(arg=f'Level: {self.score}', align='left', font=FONT)