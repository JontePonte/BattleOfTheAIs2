"""
Tournament Simulation for AI Players

This module simulates a tournament where AI players compete against each other in pairwise matches.
Each AI is represented by a function that decides whether to "attack" or "defend" based on game state.
[cue DOOM music]
"""

import pandas as pd


from play_match import play_match
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


# Find the maximum number of wins
max_wins = max(player["wins"] for player in players.values())
# Find all AIs with the maximum wins (in case of a tie)
total_winners = [player["name"] for player in players.values() if player["wins"] == max_wins]

# Print the total winners
if len(total_winners) > 1:
    winner_text = f"\nTotal Tournament Winners (tied): {', '.join(total_winners)} with {max_wins} wins each"
else:
    winner_text = f"\nTotal Tournament Winner: {total_winners[0]} with {max_wins} wins"
print(winner_text)


# Create a DataFrame for results
player_names = [player_data["name"] for player_data in players.values()]
result_matrix = [[results[p1][p2] if p1 != p2 else "-" for p2 in players] for p1 in players]

# Create Pandas DataFrame for match results
df_results = pd.DataFrame(result_matrix, index=player_names, columns=player_names)

# Print the match results table (W/L/D) in the terminal
print("\nMatch Results Table (W/L/D):")
print(df_results)


# Create a DataFrame for the leaderboard summary
leaderboard_data = {
    "Player": [player["name"] for player in players.values()],
    "Wins": [player["wins"] for player in players.values()],
    "Losses": [player["loses"] for player in players.values()],
    "Draws": [player["draws"] for player in players.values()]
}
df_leaderboard = pd.DataFrame(leaderboard_data).sort_values(by="Wins", ascending=False)

# Print the leaderboard in the terminal
print("\nLeaderboard:")
print(df_leaderboard)


# Print the moves if there is just 2 players
print(" ")
if len(players) == 2:
    player_names = list(game_info.keys())
    moves1 = game_info[player_names[0]]["moves"]
    moves2 = game_info[player_names[1]]["moves"]

    # Header, names of the AI:s
    print(f"{player_names[0]:<20} {player_names[1]:<20}")
    print("-" * 40)

    # Print the moves
    for move1, move2 in zip(moves1, moves2):
        print(f"{move1:<20} {move2:<20}")


# Save match results and leaderboard to a single CSV file
with open("tournament_results.csv", "w") as file:
    # Write the leaderboard summary to the file
    df_leaderboard.to_csv(file, index=False)
    
    # Add a blank line for separation
    file.write("\n")
    
    # Write the match results table (W/L/D)
    file.write("Match Results Table (W/L/D):\n")
    df_results.to_csv(file, index=True)
    
    # Add winner information at the end of the CSV file
    file.write("\n")
    file.write(winner_text)


# Save HTML file with the match results, leaderboard, and winner
with open("match_results.html", "w") as file:
    file.write("<h2>Match Results Table (W/L/D)</h2>")
    file.write(df_results.to_html(index=True))
    file.write("<h2>Leaderboard</h2>")
    file.write(df_leaderboard.to_html(index=False))
    file.write(f"<h3>{winner_text}</h3>")

print("\nResults, match table, leaderboard, and winner saved to match_results.html and match_results.csv")

