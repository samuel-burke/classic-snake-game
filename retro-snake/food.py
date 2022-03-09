#########################
# Author: Samuel Burke
# Created 03.05.2022
#
#########################
import random
from turtle import Turtle

import board as b

FOOD_COLOR = 'white'
FOOD_SHAPE = 'square'
FOOD_SIZE = b.BLOCK_SIZE / 40
BUFFER = 1


def get_food_coord():
    max_blocks_x = b.BLOCKS_TO_RIGHT_WALL - BUFFER
    max_blocks_y = b.BLOCKS_TO_TOP_WALL - BUFFER
    x = random.randint(-max_blocks_x, max_blocks_x) * b.BLOCK_SIZE
    y = random.randint(-max_blocks_y, max_blocks_y) * b.BLOCK_SIZE
    return x, y


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(FOOD_SIZE)
        self.color(FOOD_COLOR)
        self.move()

    def move(self):
        x, y = get_food_coord()
        self.goto(x, y)
