#Greet the user
print("Greetings! Thank you for using the Gross Income Tax Rate Calculator!")
print("-" * 50)

#Input: last name, number of dependents, gross income
name = input("Please enter your last name: ")
dependents = int(input(f"Welcome {name}, please enter the number of dependents: "))
g_income = float(input("Enter your gross income: $"))
#Embedding name directly into text source: https://realpython.com/python-f-strings/

#Compute adjusted gross income
ag_income = g_income - (dependents * 12000)

#Determine tax rate
if ag_income > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

#Compute income tax
income_tax = ag_income * tax_rate

#If income tax is less than 0, set to $100
if income_tax < 0:
    income_tax = 100.00

#Display results
print("\nLast Name:             ", name)
print("Gross Income:          ${:.2f}".format(g_income))
print("Dependents:            ", dependents)
print("Adjusted Gross Income: ${:.2f}".format(ag_income))
print("Income Tax:            ${:.2f}".format(income_tax))

#Farewell
print ("-" * 50)
print("Thank you for using the Gross Income Tax Rate Calculator! Have a pleasant day!")
