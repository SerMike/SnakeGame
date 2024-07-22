from turtle import Turtle

# Coordinates for initial snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.current_heading = RIGHT

    def create_snake(self):
        # Create initial snake length and start position
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # Link snake segments
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(UP)
        self.current_heading = UP

    def down(self):
        self.head.setheading(DOWN)
        self.current_heading = DOWN

    def left(self):
        self.head.setheading(LEFT)
        self.current_heading = LEFT

    def right(self):
        self.head.setheading(RIGHT)
        self.current_heading = RIGHT
