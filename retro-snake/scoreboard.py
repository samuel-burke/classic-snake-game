"""
Displays the Current Score and High score at the top of the screen

Author: Samuel Burke
Created: 03.05.2022
"""
import board
from text import Text


class ScoreBoard(Text):
    """
    Scoreboard object for displaying text at the top of the screen
    """

    def __init__(self):
        """Sets the current points, high score, and location of the text"""
        super().__init__()
        self.points = 0
        self.goto(0, board.TOP_WALL + 20)
        self.high_score = '0'

        # grab the high score or set to 0 if there is not a file
        try:
            with open('resources/high_score.txt', 'r') as f:
                self.high_score = f.read()
        except FileNotFoundError:
            with open('resources/high_score.txt', 'w') as f:
                f.write('0')
        if self.high_score.isnumeric():
            self.high_score = int(self.high_score)
        else:
            self.high_score = 0

        self.update_score()

    def update_score(self):
        """Refresh the score text on the screen"""
        super().update_text(f'Score: {round(self.points)}\t\t\tHigh Score: {self.high_score}')

    def update_high_score(self):
        """Resets current points and stores top score"""
        if self.points > self.high_score:
            self.high_score = self.points
        self.points = 0
        with open('resources/high_score.txt', 'w') as f:
            f.write(str(self.high_score))

    def reset_high_score(self):
        """Resets current points and top score"""
        self.points = 0
        self.high_score = 0
        with open('resources/high_score.txt', 'w') as f:
            f.write("0")

    def increment_score(self):
        """Adds one point to current score"""
        self.points += 1
