#########################
# Author: Samuel Burke
# Created 03.05.2022
#
#########################
import board
from writer import Writer


class ScoreBoard(Writer):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.goto(0, board.TOP_WALL + 20)
        self.high_score = '0'
        try:
            with open('high_score.txt', 'r') as f:
                self.high_score = f.read()
        except FileNotFoundError:
            with open('high_score.txt', 'w') as f:
                f.write('0')
        if self.high_score.isnumeric():
            self.high_score = int(self.high_score)
        else:
            self.high_score = 0
        self.update_score()

    def update_score(self):
        super().update_text(f'Score: {round(self.points)}\t\t\tHigh Score: {self.high_score}')

    def update_high_score(self):
        if self.points > self.high_score:
            self.high_score = self.points
        self.points = 0
        with open('high_score.txt', 'w') as f:
            f.write(str(self.high_score))

    def add_to_score(self, amt):
        self.points += amt
