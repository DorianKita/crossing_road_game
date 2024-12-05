import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

cars = []

for _ in range(20):
    new_car = CarManager()
    cars.append(new_car)

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move()


    player.reset_position()


