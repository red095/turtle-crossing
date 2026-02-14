import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager (Turtle):
    def __init__(self):
        super().__init__()
        self.create_cars()
        self.move_distance=STARTING_MOVE_DISTANCE
    def create_cars(self):
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1, outline=1)
        self.goto(270, random.randint(-230, 230))

    def move(self):
        self.backward(self.move_distance)


