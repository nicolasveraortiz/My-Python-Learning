from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def go_up(self):
        if not self.ycor() > 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if not self.ycor() < -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("slow")
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 1
        self.y_move = 1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def went_over(self):
        self.goto(0, 0)
        self.bounce_paddle()
