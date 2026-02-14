import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
counter=0
car_manager = CarManager()
cars= [car_manager]
game_is_on = True
while game_is_on:
    if player.ycor() > 280:
        player.refresh()
    if counter%6==0:
        new_car = CarManager()
        cars.append(new_car)
    for car in cars:
        car.move()
        if player.distance(car) < 20:
            game_is_on = False
    counter+=1
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(player.move, "Up")






