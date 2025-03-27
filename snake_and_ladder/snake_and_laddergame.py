import random

class SnakeLadder:
    def __init__(self):
        """
        Creating user 1 with starting position 0
        """
        self.position = 0

    @staticmethod
    def roll_dice():
        return random.randint(1, 6)