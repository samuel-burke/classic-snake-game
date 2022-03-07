#########################
# Author: Samuel Burke
# Created 03.05.2022
#
#########################
from turtle import Turtle

WIDTH = 620
HEIGHT = 620
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720

TOP_WALL = 310
BOTTOM_WALL = -310
RIGHT_WALL = 310
LEFT_WALL = -310

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
HEADINGS = [RIGHT, UP, LEFT, DOWN]

STEP = 20
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

    turtle.penup()
    turtle.pencolor('gray12')
    for i in range(1, WIDTH//20):
        turtle.goto(LEFT_WALL+i*20, TOP_WALL)
        turtle.pendown()
        turtle.goto(LEFT_WALL+i*20, BOTTOM_WALL)
        turtle.penup()

    for i in range(1, WIDTH//20):
        turtle.goto(LEFT_WALL, TOP_WALL-i*20)
        turtle.pendown()
        turtle.goto(RIGHT_WALL, TOP_WALL-i*20)
        turtle.penup()
