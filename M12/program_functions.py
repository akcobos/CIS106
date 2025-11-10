#Problem 1 Functions

def display_lname_list(lname_list):
    print("\nList of Last Names:")
    for index_position in range(len(lname_list)):
        print(lname_list[index_position])

def display_lname_list_reverse(lname_list):
    print("\nLast Names in Reverse Order:")
    for index_position in range(len(lname_list) - 1, -1, -1):
        print(lname_list[index_position])


#Problem 2 Functions

def display_lname_and_score(lname_list, score_list):
    print("\nStudent Exam Scores")
    print("-" * 30)
    for index_position in range(len(lname_list)):
        print(f"{lname_list[index_position]:<15} {score_list[index_position]:>6.1f}")

def display_lname_and_score_reverse(lname_list, score_list):
    print("\nStudent Exam Scores (Reverse Order)")
    print("-" * 30)
    for index_position in range(len(lname_list) - 1, -1, -1):
        print(f"{lname_list[index_position]:<15} {score_list[index_position]:>6.1f}")
       

#Problem 3 Functions

def load_data_from_file(filename, lname_list, score_list):
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            lname_list.append(parts[0])
            score_list.append(float(parts[1]))

def display_highest_score(lname_list, score_list):
    high_var = 0
    high_index = 0
    for index_position in range(len(score_list)):
        if score_list[index_position] > high_var:
            high_var = score_list[index_position]
            high_index = index_position
    print(f"\nHighest Score: {lname_list[high_index]} with {high_var:.1f}")

def display_lowest_score(lname_list, score_list):
    low_var = 999
    low_index = 0
    for index_position in range(len(score_list)):
        if score_list[index_position] < low_var:
            low_var = score_list[index_position]
            low_index = index_position
    print(f"Lowest Score: {lname_list[low_index]} with {low_var:.1f}")
       

#Problem 4 Functions

def load_player_data(filename, name_list, average_list):
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            name_list.append(parts[0])
            average_list.append(float(parts[1]))

def display_players(name_list, average_list):
    print("\nPlayer Batting Averages")
    print("-" * 30)
    for index_position in range(len(name_list)):
        print(f"{name_list[index_position]:<15} {average_list[index_position]:>6.3f}")

def search_player(name_list, average_list, search_name):
    found = False
    for index_position in range(len(name_list)):
        if name_list[index_position].lower() == search_name.lower():
            print(f"{name_list[index_position]} has a batting average of {average_list[index_position]:.3f}")
            found = True
            break
    if not found:
        print(f"{search_name} not found in the list.")
