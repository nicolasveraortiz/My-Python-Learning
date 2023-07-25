from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.multiplier = 0

    def create_new_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle()
            new_car.speed("fastest")
            new_car.penup()
            new_car.goto(300, random.randint(-260, 280))
            new_car.setheading(270)
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=2.2, stretch_len=1.3)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE-(MOVE_INCREMENT*self.multiplier)
            car.goto(new_x, car.ycor())
