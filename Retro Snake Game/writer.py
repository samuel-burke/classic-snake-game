#########################
# Author: Samuel Burke
# Created 03.05.2022
#
#########################
from turtle import Turtle
FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.font_name, self.font_pt, self.font_type = FONT
        self.hideturtle()
        self.penup()
        self.color('white')

    def update_text(self, text):
        self.clear()
        self.write(text, align=ALIGNMENT, font=(self.font_name, self.font_pt, self.font_type))
