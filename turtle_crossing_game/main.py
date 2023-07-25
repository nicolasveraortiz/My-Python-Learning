import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

juan = Player()
car = CarManager()
scoreboard = Scoreboard()
screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Juan la Tortuga")
screen.listen()
screen.onkey(juan.move_up, "Up")

game_is_on = True
while game_is_on:
    car.create_new_car()
    car.move()
    time.sleep(0.1)
    screen.update()

    if juan.ycor() > 280:
        juan.next_level()
        scoreboard.level += 1
        scoreboard.update_scoreboard()
        car.multiplier += 1

    for x in car.all_cars:
        if juan.distance(x) < 35:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
