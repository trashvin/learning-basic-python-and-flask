# the game rule processor
import random

def get_winner(player):

    if player is None:
        return 'INVALID PLAYER',''

    variables = ['Rock', 'Paper', 'Scissor', 'Lizard', 'Spock']
    computer_choice = random.randrange(0,5)
    computer = variables[computer_choice]
    if player > computer:
        return 'PLAYER',computer
    elif computer > player:
        return 'COMPUTER',computer
    else:
        return 'DRAW', computer