from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race?")
colors = ["red","orange","yellow", "green", "blue", "purple"]
y = 0
all_turtles = []
for turtle_index in range(6):
    y += 30
    r_color = random.choice(colors)
    colors.remove(r_color)
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(r_color)
    new_turtle.goto(-230, -100+y)
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You've won! The {winning_turtle} was the first!")
            else:
                print(f"You've lost... The {winning_turtle} was the first")
        r_distance = random.randint(0,10)
        turtle.forward(r_distance)
screen.exitonclick()