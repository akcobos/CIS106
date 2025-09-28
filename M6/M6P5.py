#Input the employee last name, salary, and job level
name = input("Dear user, enter employee last name: ")
salary = float(input("Enter salary: $"))
level = int(input("Enter job level: "))

#Determine bonus rate
if level >= 10:
    rate = 0.25
elif level >= 5:
    rate = 0.20
else:
    rate = 0.10

#Compute bonus
bonus = salary * rate

#Display results with aligned decimals
print("\n{:<22} {:>13}".format("Employee", name))
print("{:<22} ${:>12.2f}".format("Bonus", bonus))
