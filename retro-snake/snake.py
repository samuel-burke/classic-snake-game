"""
Manages the Snake's head and segments

Author: Samuel Burke
Created: 03.05.2022
"""
import math

from board import *

"""Default Snake Settings"""
SNAKE_COLOR = 'white'  # body color of snake
STARTING_LENGTH = 3  # number of segments for a new snake
STANDARD_SIZE = BLOCK_SIZE / 20  # Snake's scale to the grid - (do not change)


class Snake:
    """
    Snake object that controls the snake's movement of head and trailing segments.
    """

    def __init__(self, disable_key_input, length=STARTING_LENGTH):
        """
        Creates a Snake and body of chosen length
        :param disable_key_input: function that disables changing the snake heading after user input
        :param length: the starting length of the snake
        """

        self.disable_key_input = disable_key_input
        self.body = []
        for i in range(length):
            self.body.append(new_segment(-STEP * i, 0))
        self.head = self.body[0]

    def move(self):
        """
        Moves the entire snake forward with the current head heading and raises a CrashedIntoTail exception if the
        head collides with any segment of the body
        """
        heading = self.head.heading()
        head_x, head_y = self.head.position()

        # find snake head's future position after movement
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

            if distance < BLOCK_SIZE / 2:  # kill if the snake's head is hitting a body segment
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
            self.disable_key_input()
            self.head.setheading(UP)

    def down(self):
        """Points the snake's head down when the DOWN arrow key is pressed"""
        if self.head.heading() != UP:
            self.disable_key_input()
            self.head.setheading(DOWN)

    def left(self):
        """Points the snake's head left when the LEFT arrow key is pressed"""
        if self.head.heading() != RIGHT:
            self.disable_key_input()
            self.head.setheading(LEFT)

    def right(self):
        """Points the snake's head right when the RIGHT arrow key is pressed"""
        if self.head.heading() != LEFT:
            self.disable_key_input()
            self.head.setheading(RIGHT)

    def kill(self):
        """Kills the snake by recoloring the snake when it hits its tail or a wall"""
        # paints the snake the dead color
        self.head.color('gray')
        self.head.shapesize(0.4 * STANDARD_SIZE)
        for segment in self.body[1:]:
            segment.color('gray')
            segment.shapesize(0.1 * STANDARD_SIZE)

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
    segment.turtlesize(STANDARD_SIZE)
    segment.goto(x, y)
    return segment


class CrashedIntoTail(Exception):
    """Custom exception that is thrown when the Snake's head collides with a body segment"""
    pass
