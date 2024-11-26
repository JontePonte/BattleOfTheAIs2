""" Tournament Simulation for AI Players

This module simulates a tournament where AI players compete against each other in pairwise matches.
Each AI is represented by a function that decides whether to "attack" or "defend" based on game state.
[cue DOOM music]
"""

from play_match import play_match
from print_results import print_results
from registry import ai_list


# Infomation 
players = {}
for idx, ai_function in enumerate(ai_list, start=1):
    players[idx] = {
        "AI": ai_function,
        "name": ai_function.__name__,
        "wins": 0,
        "loses": 0,
        "draws": 0,
    }


# Initialize result matrix
results = {p1: {p2: None for p2 in players} for p1 in players}
winner, game_info = None, None

for player1_id, player1_data in players.items():
    for player2_id, player2_data in players.items():
        if player1_id < player2_id:  # Avoid double matches and self matches
            winner, game_info = play_match(player1_data["AI"], player2_data["AI"])

            if winner == player1_data["name"]:
                player1_data["wins"] += 1
                player2_data["loses"] += 1
                results[player1_id][player2_id] = "W"  # Win för player1
                results[player2_id][player1_id] = "L"  # Loss för player2
            elif winner == player2_data["name"]:
                player1_data["loses"] += 1
                player2_data["wins"] += 1
                results[player1_id][player2_id] = "L"  # Loss för player1
                results[player2_id][player1_id] = "W"  # Win för player2
            else:  # Draw
                player1_data["draws"] += 1
                player2_data["draws"] += 1
                results[player1_id][player2_id] = "D"  # Draw
                results[player2_id][player1_id] = "D"  # Draw

print_results(results, game_info, players)
