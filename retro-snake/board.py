#########################
# Author: Samuel Burke
# Created 03.05.2022
#
#########################
from turtle import Turtle


NUM_BLOCKS_WIDE = 21  # must be an odd value
NUM_BLOCKS_HIGH = 21  # must be an odd value
BLOCK_SIZE = 30
STEP = BLOCK_SIZE
BLOCKS_TO_RIGHT_WALL = NUM_BLOCKS_WIDE // 2
BLOCKS_TO_TOP_WALL = NUM_BLOCKS_HIGH // 2
TOP_WALL = NUM_BLOCKS_HIGH * BLOCK_SIZE // 2
RIGHT_WALL = NUM_BLOCKS_WIDE * BLOCK_SIZE // 2
BOTTOM_WALL = -TOP_WALL
LEFT_WALL = -RIGHT_WALL

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
HEADINGS = [RIGHT, UP, LEFT, DOWN]

BOARD_WIDTH = BLOCK_SIZE * NUM_BLOCKS_WIDE
BOARD_HEIGHT = BLOCK_SIZE * NUM_BLOCKS_HIGH
WINDOW_WIDTH = BOARD_WIDTH + 100
WINDOW_HEIGHT = BOARD_HEIGHT + 100

GRIDLINE_COLOR = "gray12"
BG_COLOR = 'gray8'
BORDER_COLOR = "white"


def draw_border():
    # go to the top right corner
    turtle = Turtle()
    turtle.hideturtle()
    turtle.color(BORDER_COLOR)
    turtle.penup()
    turtle.goto(LEFT_WALL, TOP_WALL)

    # draw the top, right, bottom, and left borders
    turtle.pendown()
    turtle.goto(RIGHT_WALL, TOP_WALL)
    turtle.goto(RIGHT_WALL, BOTTOM_WALL)
    turtle.goto(LEFT_WALL, BOTTOM_WALL)
    turtle.goto(LEFT_WALL, TOP_WALL)

    # draw the gridlines
    turtle.penup()
    turtle.pencolor(GRIDLINE_COLOR)
    for i in range(1, NUM_BLOCKS_WIDE):
        turtle.goto(LEFT_WALL + i*BLOCK_SIZE, TOP_WALL)
        turtle.pendown()
        turtle.goto(LEFT_WALL + i*BLOCK_SIZE, BOTTOM_WALL)
        turtle.penup()

    for i in range(1, NUM_BLOCKS_HIGH):
        turtle.goto(LEFT_WALL, TOP_WALL - i*BLOCK_SIZE)
        turtle.pendown()
        turtle.goto(RIGHT_WALL, TOP_WALL - i*BLOCK_SIZE)
        turtle.penup()
