#Function to compute tuition based on district code
def compute_tuition(credit_hours, district_code):
    district_code = district_code.upper()
    if district_code == "I":
        rate = 250
    elif district_code == "O":
        rate = 550
    else:
        rate = 0  
    return credit_hours * rate

#Begin totals
total_tuition = 0
student_count = 0

#Loop
answer = input("Would you like to enter student data? Enter Yes to continue: ")

while answer.lower() == "yes":
    #Get student data
    lastname = input("Enter student last name: ")
    credit_hours = int(input("Enter number of credit hours: "))
    district_code = input("Enter district code (I or O): ")

    #Compute tuition
    tuition = compute_tuition(credit_hours, district_code)

    #Display student info
    print("\n{:<20} {:>15}".format("Student", "Tuition Owed"))
    print("-" * 35)
    print("{:<20} {:>15}".format(lastname, f"${tuition:,.2f}"))
    print("-" * 35)

    #Update totals
    total_tuition += tuition
    student_count += 1

    #Ask to continue
    answer = input("\nWould you like to enter another student? Enter Yes to continue: ")

#Final output
print("\n{:<25} {:>12}".format("Total Tuition Owed:", f"${total_tuition:,.2f}"))
print("{:<25} {:>12}".format("Students Entered:", student_count))
