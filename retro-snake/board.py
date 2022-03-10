"""
File holds the main constants for the board parameters for all other files to reference and access the same
constants. The draw_border functionality draws the gridlines and box for the game window

Author: Samuel Burke
Created: 03.05.2022
"""

from turtle import Turtle

NUM_BLOCKS_WIDE = 21  # Number of blocks wide. Must be an odd value.
NUM_BLOCKS_HIGH = 21  # Number of blocks tall. Must be an odd value.
BLOCK_SIZE = 30  # size of each block in the board grid

"""CONSTANTS DO NOT CHANGE"""
STEP = BLOCK_SIZE
BLOCKS_TO_RIGHT_WALL = NUM_BLOCKS_WIDE // 2
BLOCKS_TO_TOP_WALL = NUM_BLOCKS_HIGH // 2
BOARD_HEIGHT = BLOCK_SIZE * NUM_BLOCKS_HIGH
BOARD_WIDTH = BLOCK_SIZE * NUM_BLOCKS_WIDE
TOP_WALL = BOARD_HEIGHT // 2
RIGHT_WALL = BOARD_WIDTH // 2
BOTTOM_WALL = -TOP_WALL
LEFT_WALL = -RIGHT_WALL
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
"""CONSTANTS DO NOT CHANGE"""

# Window padding around the game grid
PADDING = 100
WINDOW_WIDTH = BOARD_WIDTH + PADDING
WINDOW_HEIGHT = BOARD_HEIGHT + PADDING

GRID_LINE_COLOR = "gray12"  # Grid line color
BG_COLOR = 'gray8'  # Background color
BORDER_COLOR = "white"  # Border color around grid


def draw_border():
    """
    Draws the game's boarder and gridlines
    """
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
    turtle.pencolor(GRID_LINE_COLOR)
    # draw the vertical lines
    for i in range(1, NUM_BLOCKS_WIDE):
        turtle.goto(LEFT_WALL + i * BLOCK_SIZE, TOP_WALL)
        turtle.pendown()
        turtle.goto(LEFT_WALL + i * BLOCK_SIZE, BOTTOM_WALL)
        turtle.penup()
    # draw the horizontal lines
    for i in range(1, NUM_BLOCKS_HIGH):
        turtle.goto(LEFT_WALL, TOP_WALL - i * BLOCK_SIZE)
        turtle.pendown()
        turtle.goto(RIGHT_WALL, TOP_WALL - i * BLOCK_SIZE)
        turtle.penup()
