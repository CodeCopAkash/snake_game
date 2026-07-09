from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create initial 3 segment body snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        obj = Turtle(shape="square")
        obj.color("green")
        obj.penup()
        self.segments.append(obj)
        obj.goto(position)

    def extend(self):
        """Adds new segment to snake"""
        pos = self.segments[-1].position()
        self.add_segment(pos)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() == 0.0:
            self.head.left(90)
        elif self.head.heading() == 180.0:
            self.head.right(90)

    def down(self):
        if self.head.heading() == 0.0:
            self.head.right(90)
        elif self.head.heading() == 180.0:
            self.head.left(90)

    def left(self):
        if self.head.heading() == 90.0:
            self.head.left(90)
        elif self.head.heading() == 270.0:
            self.head.right(90)

    def right(self):
        if self.head.heading() == 90.0:
            self.head.right(90)
        elif self.head.heading() == 270.0:
            self.head.left(90)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
