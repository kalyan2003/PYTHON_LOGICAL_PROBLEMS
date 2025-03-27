import random

class SnakeLadder:
    def __init__(self):
        self.position = 0
        self.dice_rolls = 0

    @staticmethod
    def roll_dice():
        return random.randint(1, 6)

    def play_turn(self):
        dice_value = SnakeLadder.roll_dice()
        self.dice_rolls += 1
        option = random.choice(["No play", "Ladder", "Snake"])

        if option == "No play":
            pass
        elif option == "Ladder":
            if self.position + dice_value <= 100:
                self.position += dice_value
        elif option == "Snake":
            self.position -= dice_value
            if self.position < 0:
                self.position = 0

        print(f"Dice rolled: {dice_value}, Option: {option}, New Position: {self.position}")

    def play_game(self):
        while self.position < 100:
            self.play_turn()

        print(f"Game Over! Player reached 100 in {self.dice_rolls} rolls.")

game = SnakeLadder()
game.play_game()
