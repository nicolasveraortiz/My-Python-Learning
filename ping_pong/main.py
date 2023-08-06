from paddle import Paddle, Ball
from turtle import Screen
from scoreboard import Scoreboard
import time


def increase_speed(time_sleep):
    if time_sleep > 0.00020:
        time_sleep -= 0.00020
    return time_sleep


r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
screen = Screen()
scoreboard = Scoreboard()
screen.setup(800, 600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.tracer(0)
timer = 0.00200

is_game_on = True
while is_game_on:
    time.sleep(timer)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_paddle()
        timer = increase_speed(timer)
    if ball.xcor() > 390:
        ball.went_over()
        timer = 0.00200
        scoreboard.l_point()
    if ball.xcor() < -390:
        ball.went_over()
        timer = 0.00200
        scoreboard.r_point()

screen.exitonclick()
