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

    def play_turn(self):
        dice_value = SnakeLadder.roll_dice()  
        option = random.choice(["No Play", "Ladder", "Snake"])

        if option == "No Play":
            pass
        elif option == "Ladder":
            self.position += dice_value
        elif option == "Snake":
            self.position -= dice_value
            if self.position < 0:
                self.position = 0

        print(f"Dice rolled: {dice_value}, Option: {option}, New Position: {self.position}")


game = SnakeLadder()
game.play_turn()
