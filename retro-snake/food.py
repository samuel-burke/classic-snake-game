"""
Handles the food that is displayed on the screen for the snake to eat.

Author: Samuel Burke
Created: 03.05.2022
"""
import random
from turtle import Turtle

import board as b

FOOD_COLOR = 'white'  # Color of the food piece
FOOD_SHAPE = 'square'  # The shape of the food piece
FOOD_SIZE = b.BLOCK_SIZE / 40  # the food's scale to the grid
"""
How close the food can spawn to the edges of the board. 
0=food can spawn anywhere, 
1=food can spawn anywhere that is not touching an edge
2=food can spawn anywhere that is not touching a block that is touching an edge
etc.
"""
BUFFER = 1


def get_food_coord():
    """
    Generates a random (x,y) point for the food that is within the grid of the board and not outside the buffer
    :return: the (x, y) point
    """
    max_blocks_x = b.BLOCKS_TO_RIGHT_WALL - BUFFER
    max_blocks_y = b.BLOCKS_TO_TOP_WALL - BUFFER
    x = random.randint(-max_blocks_x, max_blocks_x) * b.BLOCK_SIZE
    y = random.randint(-max_blocks_y, max_blocks_y) * b.BLOCK_SIZE
    return x, y


class Food(Turtle):
    """
    Food object that represents a piece of food on the game grid
    """

    def __init__(self):
        """
        Creates a food instance and sends it to a random position on the board
        """
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(FOOD_SIZE)
        self.color(FOOD_COLOR)
        self.move()

    def move(self):
        """
        Moves the piece of food to a new random (x, y) point
        """
        x, y = get_food_coord()
        self.goto(x, y)
