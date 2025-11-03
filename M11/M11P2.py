from program_functions import compute_scores

student_count = 0
total_all_points = 0
total_all_averages = 0

answer = input("Would you like to enter student scores? Enter Yes to continue: ")

while answer.lower() == "yes":
    last_name = input("Enter student's last name: ")
    exam1 = float(input("Enter exam score 1: "))
    exam2 = float(input("Enter exam score 2: "))
    exam3 = float(input("Enter exam score 3: "))

    total_points, average_score = compute_scores(exam1, exam2, exam3)

    print("\nExam Score Summary")
    print("-" * 40)
    print(f"{'Student:':<25}{last_name:>15}")
    print(f"{'Total points:':<25}{total_points:>15.2f}")
    print(f"{'Average score:':<25}{average_score:>15.2f}")
    print("-" * 40)

    student_count += 1
    total_all_points += total_points
    total_all_averages += average_score

    answer = input("\nWould you like to enter another student? Enter Yes to continue: ")

print("\nSummary of All Students")
print("-" * 40)
print(f"{'Total students entered:':<25}{student_count:>15.2f}")
print(f"{'Total points:':<25}{total_all_points:>15.2f}")
print(f"{'Average of all averages:':<25}{(total_all_averages / student_count):>15.2f}")
print("-" * 40)
