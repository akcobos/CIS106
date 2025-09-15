import time
#Greeting
print("Hello! Welcome to The Exam Score Calculator!")
time.sleep(2)
print("-" * 50)
#Step by step process of what the user needs to do to find exam scores
print("This score will be based on two exam scores which you will enter.")
time.sleep(3)
print("Your first exam is worth 60% of your total score, while the second is worth 40%")
print("-" * 50)
time.sleep(2)
#Get user input
first_exam = float(input("Enter your score for the first exam (0-100): "))
second_exam = float(input("Enter your score for the second exam (0-100): "))
print("-" * 50)
#Calculate weighted total
print("Calculating your total weighted score... please wait")
time.sleep(2)
weighted_first = first_exam * 0.6
weighted_second = second_exam * 0.4
total_score = weighted_first + weighted_second
print("Loading...")
time.sleep (2)
print("-" * 50)
#Display results
print(f"Your total weighted score is: {total_score:2f}")

