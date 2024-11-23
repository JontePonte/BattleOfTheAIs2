import inspect

def mixtral_1(game_info):
    """ An adaptive AI that adjusts its strategy based on the opponent's moves. """

    # Unpack game info
    my_health, my_moves = None, None
    opponent_health, opponent_moves = None, None

    for ai_name, ai_data in game_info.items():
        if ai_name == inspect.currentframe().f_code.co_name:
            my_health = ai_data['health']
            my_moves = ai_data['moves']
        else:
            opponent_health = ai_data['health']
            opponent_moves = ai_data['moves']

    # Adapt the AI's strategy based on its own health
    if my_health < 3:
        action = "rebuild"
    elif opponent_health < 3:
        action = "attack"
    else:
        action = "defend"

    return action
