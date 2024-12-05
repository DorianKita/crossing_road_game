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
scoreboard = Scoreboard()

cars = []

for _ in range(20):
    new_car = CarManager()
    cars.append(new_car)

screen.listen()
screen.onkey(player.move, "w")
speed = 0.1
game_is_on = True
while game_is_on:

    time.sleep(speed)
    screen.update()

    for car in cars:
        car.move()

    if player.ycor() == 280:
        player.reset_position()
        scoreboard.change_level()
        speed *= 0.50



