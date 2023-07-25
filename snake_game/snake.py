from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.all_segments.append(snake)

    def extend(self):
        self.add_segment(self.all_segments[-1].position())

    def move(self):
        for snake_num in range(len(self.all_segments) - 1, 0, -1):
            x = self.all_segments[snake_num - 1].xcor()
            y = self.all_segments[snake_num - 1].ycor()
            self.all_segments[snake_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.all_segments:
            seg.goto(1000,1000)
        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]