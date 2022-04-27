# the game rule processor
import random

def get_winner(player):

    if player is None:
        return 'INVALID PLAYER',''

    variables = ['Rock', 'Paper', 'Scissor', 'Lizard', 'Spock']
    computer_choice = random.randrange(0,5)
    computer = variables[computer_choice]

    # do you your changes below, replace the if condition that matches the rules

    # Scissors cuts Paper,  Paper covers Rock,  Rock crushes Lizard,
    # Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard,
    # Lizard eats Paper,  Paper disproves Spock, Spock vaporizes Rock,
    # (and as it always has) Rock crushes Scissors
    
    if player > computer:
        return 'PLAYER',computer
    elif computer > player:
        return 'COMPUTER',computer
    else:
        return 'DRAW', computer