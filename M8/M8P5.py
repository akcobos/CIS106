#Open and read the student data file
with open("students.txt", "r") as file:
    lines = file.readlines()

#Begin totals
total_tuition = 0.0
student_count = 0
print(f"{'Last Name':<15}{'Credits':>10}{'Tuition':>15}")
print("-" * 50)

#Process each student 
for i in range(0, len(lines), 3):
    last_name = lines[i].strip()
    district_code = lines[i + 1].strip().upper()
    credits = int(lines[i + 2].strip())

    #Determine cost per credit
    if district_code == "I":
        cost_per_credit = 250.00
    else:
        cost_per_credit = 500.00

    #Calculate tuition
    tuition = credits * cost_per_credit
    total_tuition += tuition
    student_count += 1

    #Display student info
    print(f"{last_name:<15}{credits:>10}{tuition:>15,.2f}")
    print("-" * 50)

#Display summary
print("\nSummary:")
print("-"*50)
print(f"{'Total tuition owed:':<25}${total_tuition:10,.2f}")
print(f"{'Number of students:':<25}{student_count:>10}")
