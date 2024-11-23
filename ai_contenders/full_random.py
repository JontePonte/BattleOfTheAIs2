"""
Random choice AI
Name: full_random
"""

import inspect
import random


def full_random(game_info):
    """ Random choise between attack and defend """

    # Unpack game info
    my_health, my_moves = None, None, None
    opponent_health, opponent_moves = None, None, None
    
    for ai_name in game_info:
        if ai_name == inspect.currentframe().f_code.co_name:
            my_health = game_info[ai_name]['health']
            my_moves = game_info[ai_name]['moves']
        else:
            opponent_health = game_info[ai_name]['health']
            opponent_moves = game_info[ai_name]['moves']

    action = random.choice(["attack", "defend", "rebuild"])

    return action