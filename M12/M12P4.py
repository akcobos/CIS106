#Import functions
from program_functions import (
    load_player_data,
    display_players,
    search_player
)

#Arrays
name_list = []
average_list = []

#Load data from file
load_player_data("player_averages.txt", name_list, average_list)
display_players(name_list, average_list)

#Search loop
while True:
    search_name = input("\nEnter a player's last name to search (or type 'exit' to quit): ")
    if search_name.lower() == "exit":
        print("Exiting search.")
        break
    search_player(name_list, average_list, search_name)
