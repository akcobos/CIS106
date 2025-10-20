#Compute batting average
def compute_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0.0  
    return hits / at_bats

#Begin player counter
player_count = 0

#Loop
answer = input("Would you like to enter player stats? Enter Yes to continue: ")

while answer.lower() == "yes":
    #Get player data
    lastname = input("Enter player's last name: ")
    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at-bats: "))

    #Compute batting average
    average = compute_batting_average(hits, at_bats)

    #Display Player's names and battling averages
    print("\n{:<15} {:>15}".format("Player", "Batting Average"))
    print("-" * 30)
    print("{:<15} {:>15.3f}".format(lastname, average))
    print("-" * 30)

    #Increment player count
    player_count += 1

    #Ask to continue
    answer = input("\nWould you like to enter another player? Enter Yes to continue: ")

#Final output
print("\nTotal Players Entered: {}".format(player_count))
