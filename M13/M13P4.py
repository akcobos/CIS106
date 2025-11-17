
from program_functions import load_player_data, search_player

players = load_player_data("player_averages.txt")

while True:
    search_name = input("\nEnter a player's last name (or 'exit' to quit): ")
    if search_name.lower() == "exit":
        print("Exiting search.")
        break
    search_player(players, search_name)
