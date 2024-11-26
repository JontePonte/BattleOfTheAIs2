""" Countering Ai """

import inspect
import random


def counter_player(game_info):
    """ Random choise between attack and defend """

    # Unpack game info
    my_health, my_moves = None, None
    opponent_health, opponent_moves = None, None
    
    for ai_name in game_info:
        if ai_name == inspect.currentframe().f_code.co_name:
            my_health = game_info[ai_name]['health']
            my_moves = game_info[ai_name]['moves']
        else:
            opponent_health = game_info[ai_name]['health']
            opponent_moves = game_info[ai_name]['moves'] 

    last_opponent_move = opponent_moves[-1] if opponent_moves else None

    if last_opponent_move == "attack":
        return "defend"  # Counter attack
    elif last_opponent_move == "defend":
        return "rebuild" # Try to break through
    elif last_opponent_move == "rebuild":
        return "attack"  # Take advantage of their rebuilding
    else:
        return random.choice(["attack", "defend", "rebuild"])  # Default to random