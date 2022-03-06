#########################
# Author: Samuel Burke
# Created 03.05.2022
#
#########################
from turtle import Turtle

WIDTH = 820
HEIGHT = 820
WINDOW_WIDTH = 920
WINDOW_HEIGHT = 920

TOP_WALL = 410
BOTTOM_WALL = -410
RIGHT_WALL = 410
LEFT_WALL = -410

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
HEADINGS = [RIGHT, UP, LEFT, DOWN]

STEP = 10
TURTLE_SIZE = 20


def draw_border():
    # go to the top right corner
    turtle = Turtle()
    turtle.hideturtle()
    turtle.color('white')
    turtle.penup()
    turtle.goto(LEFT_WALL, TOP_WALL)

    # draw the top, right, bottom, and left borders
    turtle.pendown()
    turtle.goto(RIGHT_WALL, TOP_WALL)
    turtle.goto(RIGHT_WALL, BOTTOM_WALL)
    turtle.goto(LEFT_WALL, BOTTOM_WALL)
    turtle.goto(LEFT_WALL, TOP_WALL)
