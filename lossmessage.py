#########################
# Author: Samuel Burke
# Created 03.05.2022
#
#########################
from writer import Writer


class LossMessage(Writer):
    def __init__(self):
        super().__init__()
        self.font_pt = 30

    def display(self):
        super().update_text('Press Space to play again!')
