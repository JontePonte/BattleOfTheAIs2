
import pandas as pd



def print_results(results, game_info, players):
    """ Function that handles all the prints and visualisation """
    # Find the maximum number of wins
    max_wins = max(player["wins"] for player in players.values())

    # Find all AIs with the maximum wins
    potential_winners = [player for player in players.values() if player["wins"] == max_wins]

    # If there's a tie in wins, check for draws to determine the winner
    if len(potential_winners) > 1:
        max_draws = max(player["draws"] for player in potential_winners)
        total_winners = [player["name"] for player in potential_winners if player["draws"] == max_draws]
    else:
        total_winners = [potential_winners[0]["name"]]

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
    df_leaderboard = pd.DataFrame(leaderboard_data).sort_values(by=["Wins", "Draws"], ascending=False)

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
        print(f"{player_names[0]:<20} {game_info[player_names[0]]["health"]:<4} {player_names[1]:<20} {game_info[player_names[1]]["health"]:<4}")
        print("-" * 40)

        # Print the moves
        for move1, move2 in zip(moves1, moves2):
            print(f"{move1:<25} {move2:<25}")


    # Save match results and leaderboard to a single CSV file
    with open("tournament_results.csv", "w", encoding="utf-8") as file:
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
    with open("match_results.html", "w", encoding="utf-8") as file:
        file.write("<h2>Match Results Table (W/L/D)</h2>")
        file.write(df_results.to_html(index=True))
        file.write("<h2>Leaderboard</h2>")
        file.write(df_leaderboard.to_html(index=False))
        file.write(f"<h3>{winner_text}</h3>")

    print("\nResults, match table, leaderboard, and winner saved to match_results.html and match_results.csv")

