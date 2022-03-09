#########################
# Author: Samuel Burke
# Created 03.05.2022
#
#########################
import math
from board import *

'''Default Snake Settings'''
SNAKE_COLOR = 'white'
STARTING_LENGTH = 3


class Snake:
    def __init__(self, screen, length=STARTING_LENGTH):
        self.screen = screen
        self.body = []
        for i in range(length):
            self.body.append(new_segment(-STEP * i, 0))
        self.head = self.body[0]

    def move(self):
        """Moves the entire snake forward with the current head heading and raises a CrashedIntoTail exception if the
        head collides with any segment of the body"""
        heading = self.head.heading()
        head_x, head_y = self.head.position()

        # find snake head's future x,y after movement
        if heading == RIGHT:
            head_x += STEP
        elif heading == UP:
            head_y += STEP
        elif heading == LEFT:
            head_x -= STEP
        else:
            head_y -= STEP

        # check if the head will crash into any segment of the tail
        for segment in self.body:
            distance = math.dist((head_x, head_y), segment.position())

            if distance < 10:  # kill if the snake's head is less than 10 from a body segment
                self.kill()
                raise CrashedIntoTail()

        # move each segment to the location of the segment in front of it
        for i in range(len(self.body) - 1, 0, -1):
            x, y = self.body[i - 1].position()
            self.body[i].goto(x, y)

        # finally, move the head to its new location
        self.head.goto(head_x, head_y)

    def up(self):
        """Points the snake's head up when the UP arrow key is pressed"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.screen.onkey(None, 'Up')
            self.screen.onkey(None, 'Down')
            self.screen.onkey(None, 'Left')
            self.screen.onkey(None, 'Right')

    def down(self):
        """Points the snake's head down when the DOWN arrow key is pressed"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.screen.onkey(None, 'Up')
            self.screen.onkey(None, 'Down')
            self.screen.onkey(None, 'Left')
            self.screen.onkey(None, 'Right')

    def left(self):
        """Points the snake's head left when the LEFT arrow key is pressed"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.screen.onkey(None, 'Up')
            self.screen.onkey(None, 'Down')
            self.screen.onkey(None, 'Left')
            self.screen.onkey(None, 'Right')

    def right(self):
        """Points the snake's head right when the RIGHT arrow key is pressed"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.screen.onkey(None, 'Up')
            self.screen.onkey(None, 'Down')
            self.screen.onkey(None, 'Left')
            self.screen.onkey(None, 'Right')

    def kill(self):
        """Kills the snake by recoloring the snake when it hits its tail or a wall"""
        # paints the snake the dead color
        self.head.color('gray')
        self.head.shapesize(0.4)
        for segment in self.body[1:]:
            segment.color('gray')
            segment.shapesize(0.1)

    def grow(self, n=1):
        """Adds n segments to the snakes body"""

        # check if there are any more segments to add
        if n < 1:
            return
        # add 1 segment
        else:
            # get the tail's (x, y)
            tail = self.body[-1]
            tail_x, tail_y = tail.position()

            # add the segment to the end of the tail
            self.body.append(new_segment(tail_x, tail_y))
            self.grow(n - 1)  # recursively call grow() until there are no more segments to add


def new_segment(x, y):
    """Generates a new segment for the snake body"""
    segment = Turtle('square')
    segment.speed('fastest')
    segment.penup()
    segment.color(SNAKE_COLOR)
    segment.turtlesize(1)
    segment.goto(x, y)
    return segment


class CrashedIntoTail(Exception):
    """Custom exception that is thrown when the Snake's head collides with a body segment"""
    pass
