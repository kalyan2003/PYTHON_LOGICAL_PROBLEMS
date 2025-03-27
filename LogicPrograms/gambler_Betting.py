
import random

stake = int(input("Enter the stake amount: "))
goal = int(input("How much you want to earn: "))
no_of_times = int(input("Enter number of times you play: "))

def calculate_gambler_won_lost_percentage(stake, goal, no_of_times):
    """
    Simulates a gambler's game and calculates win/loss percentages.

    Arguments:
    stake (int): Initial amount the gambler has.
    goal (int): Target amount the gambler wants to reach.
    no_of_times (int): Number of times the game is played.

    Returns:
    Tuple: (Win/Loss status, percentage of losses, percentage of wins)
    """

    original_no_of_times = no_of_times  
    gambler_wins = 0
    gambler_loss = 0

    while stake > 0 and stake < goal and no_of_times > 0:
        if random.choice([0, 1]) == 0:
            stake -= 1
            gambler_loss += 1
        else:
            stake += 1
            gambler_wins += 1
        
        no_of_times -= 1  

   
    gambler_status = "won" if stake == goal else "lost"


    loss_percentage = (gambler_loss / original_no_of_times) * 100
    win_percentage = (gambler_wins / original_no_of_times) * 100

    return gambler_status, loss_percentage, win_percentage

# Run the function
gambler_game_status, gl_percentage, gw_percentage = calculate_gambler_won_lost_percentage(stake, goal, no_of_times)

print(f"Gambler won or lost? {gambler_game_status}")
print(f"Gambler win percentage: {gw_percentage:.2f}%")
print(f"Gambler loss percentage: {gl_percentage:.2f}%")
