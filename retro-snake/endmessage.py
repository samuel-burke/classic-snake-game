#########################
# Author: Samuel Burke
# Created 03.05.2022
#
#########################
from writer import Writer


class EndMessage(Writer):
    def __init__(self):
        super().__init__()
        self.font_pt = 30

    def display(self, text):
        super().update_text(text)
