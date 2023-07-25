from paddle import Paddle, Ball
from turtle import Screen
import time
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
screen = Screen()
screen.setup(800, 600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.tracer(0)


is_game_on = True

while is_game_on:
    
    screen.update()
    ball.move()
screen.exitonclick()
