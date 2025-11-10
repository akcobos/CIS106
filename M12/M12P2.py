#import functions

from program_functions import display_lname_and_score, display_lname_and_score_reverse

#Parallel arrays
lname_list = ["Goldberg", "Bryant", "Castro", "D'Amelio", "Eckhart",
              "Kim", "Gonzalez", "Frye", "Reitsma", "Nguyen"]

score_list = [88.5, 92.0, 76.5, 85.0, 90.5, 79.0, 94.5, 81.0, 87.5, 89.0]

#Display names and scores
display_lname_and_score(lname_list, score_list)

#Reverse
display_lname_and_score_reverse(lname_list, score_list)
