"""
Text class that has a common theme and can update the text on the screen

Author: Samuel Burke
Created: 03.05.2022
"""
from turtle import Turtle

FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'


class Text(Turtle):
    """Text parent class with font presets for child instances"""

    def __init__(self):
        """Set the font presets"""
        super().__init__()
        self.font_name, self.font_pt, self.font_type = FONT
        self.hideturtle()
        self.penup()
        self.color('white')

    def update_text(self, text):
        """Update the text field on the screen"""
        self.clear()
        self.write(text, align=ALIGNMENT, font=(self.font_name, self.font_pt, self.font_type))
