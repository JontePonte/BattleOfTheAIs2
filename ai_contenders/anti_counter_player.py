import inspect
import random


def anti_counter_player(game_info):
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


    # last_opponent_move = opponent_moves[-1] if opponent_moves else None

    # if last_opponent_move == "attack":
    #     return "defend"  # Counter attack
    # elif last_opponent_move == "defend":
    #     return "rebuild"  # Try to break through
    # elif last_opponent_move == "rebuild":
    #     return "attack"  # Take advantage of their rebuilding
    # else:
    #     return random.choice(["attack", "defend", "rebuild"])  # Default to random

    my_last_move = my_moves[-1] if my_moves else None

    if my_last_move == "attack": # If I attacked last round counter_player will defend
        action = "rebuild"
    elif my_last_move == "defend": # He will rebuild if I defended last round
        action = "attack"
    elif my_last_move == "rebuild":
        action = "defend"
    else:
        action = random.choice(["attack", "defend", "rebuild"])
    
    return action

