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
FOOD_SIZE = 0.5
BUFFER = 50


def get_food_coord():
    amt = (b.WIDTH - 2 * BUFFER) // 2
    x = random.randint(-amt, amt) // 20 * 20
    y = random.randint(-amt, amt) // 20 * 20
    return x, y


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.setheading(random.choice(b.HEADINGS))
        self.penup()
        self.shapesize(FOOD_SIZE)
        self.color(FOOD_COLOR)
        self.move()

    def move(self):
        x, y = get_food_coord()
        self.goto(x, y)
        self.setheading(random.choice(b.HEADINGS))
