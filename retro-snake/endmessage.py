"""
Author: Samuel Burke
Created: 03.05.2022
"""
from text import Text


class EndMessage(Text):
    """
    Writer instance that is positioned in the center of the screen to display the message for when the
    gameplay is over.
    """

    def __init__(self):
        """
        Sets font and location to center
        """
        super().__init__()
        self.font_pt = 30

    def display(self, text):
        """
        Updates the text to display
        :param text: the new text
        """
        super().update_text(text)
