

def play_round(player1_move, player2_move, game_info):
    """Play one round between player 1 and player 2"""

    player1_name = list(game_info.keys())[0]
    player2_name = list(game_info.keys())[1]

    # Unpack game info
    player1_health = game_info[player1_name]['health']
    player1_moves = game_info[player1_name]['moves']

    player2_health = game_info[player2_name]['health']
    player2_moves = game_info[player2_name]['moves']


    # Player 1 attack
    if player1_move == "attack":
        player1_moves.append("attack")

        if player2_move == "attack":        
            player1_health += -1
            player2_health += -1
            player2_moves.append("attack")

        elif player2_move == "defend":
            player1_health += -1
            player2_health += 0
            player2_moves.append("defend")
        
        elif player2_move == "rebuild":
            player1_health += 0
            player2_health += -2
            player2_moves.append("rebuild")
    
    # Player 1 defend
    elif player1_move == "defend":
        player1_moves.append("defend")

        if player2_move == "attack":        
            player1_health += 0
            player2_health += -1
            player2_moves.append("attack")

        elif player2_move == "defend":
            player1_health += 0
            player2_health += 0
            player2_moves.append("defend")
        
        elif player2_move == "rebuild":
            player1_health += 0
            player2_health += 1
            player2_moves.append("rebuild")
    
    # Player 1 rebuild
    elif player1_move == "rebuild":
        player1_moves.append("rebuild")

        if player2_move == "attack":        
            player1_health += -2
            player2_health += 0
            player2_moves.append("attack")

        elif player2_move == "defend":
            player1_health += 1
            player2_health += 0
            player2_moves.append("defend")
        
        elif player2_move == "rebuild":
            player1_health += 1
            player2_health += 1
            player2_moves.append("rebuild")


    # Store new game info
    new_game_info = {
        player1_name: {
            "health": player1_health,
            "moves": player1_moves
        },
        player2_name: {
            "health": player2_health,
            "moves": player2_moves
        }
    }

    return new_game_info

