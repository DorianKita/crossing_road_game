from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 15
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.position_y = random.randint(-250,250)
        self.position_x = random.randint(300, 1000)
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=1.7)
        self.color(random.choice(COLORS))
        self.goto(self.position_x, self.position_y)


    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.position_y)
        if new_x <-300:
            new_x = random.randint(300, 1000)
            new_y = random.randint(-250,250)
            self.goto(new_x, new_y)

    def generate_new_starting_point(self):
        self.goto(x=self.position_x, y=self.position_y)