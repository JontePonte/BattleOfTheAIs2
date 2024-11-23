Battle of the AI:s version 2 is out!
Players now have the choice to choose the new "rebuild" move and don't have to worry about any stupid points. Just kill the opponent or be stronger after 10 rounds.


Here's some instructions to past in AI helper:

Hi! We're playing a game in my AI-class. It's a tournament were all students create there own ai. By the end everyone will face each other and the student with most wins win a price. The game is played one on one in matches of 10 rounds. The players start with 5 health. If any player reach 0 health the match is over and the living player wins. It's a draw if both reaches 0 health in the same round. If both players are alive after 10 rounds the one with most health wins or draw if both have the same health.
Before each round the players choose one of three moves: attack, defend or rebuild.
Players loose or gain health based of their choices. The matrix below shows the health gain/loss for player1 column, and player2 rows: 

                   attack                  defend              rebuild
attack             -1                      -1                  +0
defend             +0                      +0                  +0
rebuild            -2                      +1                  +1




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
