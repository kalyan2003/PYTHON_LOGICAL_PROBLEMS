import random

class TicTacToe:
    def __init__(myObject):
        myObject.board = [" " for _ in range(9)] 
        myObject.current_winner = None

    def print_board(myObject):
        """
        Prints the Tic-Tac-Toe board.
        """
        for row in [myObject.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def available_moves(myObject):
        """
        Returns available move positions.
        """
        return [i for i in range(9) if myObject.board[i] == " "]

    def make_move(myObject, position, letter):
        """
        Makes a move based on the position given by the user and checks for a winner.
        """
        if myObject.board[position] == " ":
            myObject.board[position] = letter
            if myObject.check_winner(position, letter):
                myObject.current_winner = letter
            return True
        return False

    def check_winner(myObject, position, letter):
        """
        Checks if a player has won.
        """
        row_ind = position // 3
        row = myObject.board[row_ind * 3:(row_ind + 1) * 3]
        if all(s == letter for s in row):  # Checking rows
            return True

        col_ind = position % 3
        column = [myObject.board[col_ind + i * 3] for i in range(3)]
        if all(s == letter for s in column):  # Checking  columns
            return True

        if position % 2 == 0:  # Checking  diagonals
            diagonal1 = [myObject.board[i] for i in [0, 4, 8]]
            diagonal2 = [myObject.board[i] for i in [2, 4, 6]]
            if all(s == letter for s in diagonal1) or all(s == letter for s in diagonal2):
                return True

        return False

    def is_full(myObject):
        """Checks if the board is full (draw)."""
        return " " not in myObject.board

def play_game():
    game = TicTacToe()
    player = "X"
    computer = "O"

    while True:
        game.print_board()
        if game.is_full():
            print("It's a tie!")
            break

        if game.current_winner:
            print(f"{game.current_winner} wins!")
            break

        if player == "X":
            try:
                position = int(input("Enter your move (0-8): "))
                if position not in game.available_moves():
                    print("Invalid move! Try again.")
                    continue
            except ValueError:
                print("Please enter a number between 0-8.")
                continue
        else:
            position = random.choice(game.available_moves()) 
            print(f"Computer chooses: {position}")

        game.make_move(position, player)
        player = "O" if player == "X" else "X"  

if __name__ == "__main__":
    play_game()
