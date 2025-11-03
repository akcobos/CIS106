from program_functions import compute_bowling_scores

# Initialize summary variables
total_average = 0
total_adjusted = 0
entry_count = 0

# Loop control
answer = input("Would you like to enter bowling scores? Enter Yes to continue: ")

while answer.lower() == "yes":
    last_name = input("Enter bowler's last name: ")
    score1 = float(input("Enter game score 1: "))
    score2 = float(input("Enter game score 2: "))
    score3 = float(input("Enter game score 3: "))
    handicap = float(input("Enter handicap: "))

    average, adjusted_average = compute_bowling_scores(score1, score2, score3, handicap)

    print("\n\tBowling Score Report")
    print("-" * 40)
    print(f"{'Bowler:':<31} {last_name}")
    print(f"{'Average score:':<25} {average:>10.2f}")
    print(f"{'Average with handicap:':<25} {adjusted_average:>10.2f}")
    print("-" * 40)

    total_average += average
    total_adjusted += adjusted_average
    entry_count += 1

    answer = input("\nWould you like to enter another bowler? Enter Yes to continue: ")

# Final summary
print("\n\tSummary of All Bowlers")
print("-" * 40)
print(f"{'Total entries:':<25}{entry_count:>15.2f}")
print(f"{'Total average score:':<25}{total_average:>15.2f}")
print(f"{'Total adjusted score:':<25}{total_adjusted:>15.2f}")
print("-" * 40)
