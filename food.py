#########################
# Author: Samuel Burke
# Created 03.05.2022
#
#########################
import random
from turtle import Turtle

import board as b

FOOD_COLOR = 'silver'
FOOD_SHAPE = 'turtle'
FOOD_SIZE = 1.5
BUFFER = 50
CRAWL_SPEED = 0.5


def get_food_coord():
    amt = (b.WIDTH - 2 * BUFFER) // 2
    x = random.randint(-amt, amt)
    y = random.randint(-amt, amt)
    return x, y


class Food(Turtle):

    def __init__(self, can_crawl=True):
        super().__init__()
        self.can_crawl = can_crawl
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

    def forward(self):
        if self.can_crawl:
            if self.heading() == b.RIGHT and b.RIGHT_WALL - self.xcor() < BUFFER:
                self.setheading(b.LEFT)
            elif self.heading() == b.LEFT and self.xcor() - b.LEFT_WALL < BUFFER:
                self.setheading(b.RIGHT)
            elif self.heading() == b.UP and b.TOP_WALL - self.ycor() < BUFFER:
                self.setheading(b.DOWN)
            elif self.heading() == b.DOWN and self.ycor() - b.BOTTOM_WALL < BUFFER:
                self.setheading(b.UP)
            super().forward(CRAWL_SPEED)
