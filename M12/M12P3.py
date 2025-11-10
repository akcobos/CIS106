#Import functions

from program_functions import (
    load_data_from_file,
    display_lname_and_score,
    display_highest_score,
    display_lowest_score
)

#Arrays
lname_list = []
score_list = []

#Load data
load_data_from_file("lname_scores.txt", lname_list, score_list)

# Display all data
display_lname_and_score(lname_list, score_list)
display_highest_score(lname_list, score_list)
display_lowest_score(lname_list, score_list)

