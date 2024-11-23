Battle of the AI:s version 2 is out!
Players now have the choice to choose the new "rebuild" move and don't have to worry about any stupid points. Just kill the opponent or be stronger after 10 rounds.


Here's some instructions to past in AI helper:

                   attack                  defend              rebuild
attack             -1                      -1                  +0
defend             +0                      +0                  +0
rebuild            -2                      +2                  +1

The ai:s will be written in this format:

import inspect
import random

def full_random(game_info):
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

    action = random.choice(["attack", "defend", "rebuild"])

    return action
