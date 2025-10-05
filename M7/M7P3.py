#Assign beginning value to student counter
count = 0

#First prompt before the loop
answer = input("Do you want to run the program? (Yes to continue): ")
print("-" *50)

#Loop control: continue only if answer is "Yes" or "yes"
while answer == "Yes" or answer == "yes":
    #Input student data
    name = input("Enter student's last name: ")
    score1 = float(input("Enter first exam score: "))
    score2 = float(input("Enter second exam score: "))

    #Calculate average
    average = (score1 + score2) / 2

    #Display result
    print("\n{:<20} {:>10}".format("Student", "Average Score"))
    print("{:<20} {:>10.2f}".format(name, average))
    print("-" * 50)

    #Increment counter
    count = count + 1

    #Prompt again inside the loop
    answer = input("Do you want to run the program again? (Yes to continue): ")

#After loop ends
print("Total students entered:", count)
