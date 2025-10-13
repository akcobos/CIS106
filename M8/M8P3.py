#Open and read employee data file
with open("employees.txt", "r") as file:
    lines = file.readlines()

#Total bonus
total_bonus = 0.0
print(f"{'Last Name':<15}{'Salary':>12}{'Bonus':>10}")

#Process each employee
for i in range(0, len(lines), 2):
    last_name = lines[i].strip()
    salary = float(lines[i + 1].strip())

    #Determine bonus rate
    if salary >= 100000.00:
        rate = 0.20
    elif salary == 50000.00:
        rate = 0.15
    else:
        rate = 0.10

    #Calculate bonus
    bonus = salary * rate
    total_bonus += bonus

    #Display employee info
    print(f"{last_name:<15}${salary:>10,.2f}${bonus:>10,.2f}")

#Display total bonus paid
print(f"\nTotal bonuses paid: ${total_bonus:,.2f}")
