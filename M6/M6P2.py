#Input the part number and quantity
part = input("Dear user, enter part number: ")
quantity = int(input("Enter quantity: "))
print("-" * 50)

#Determine unit cost 
if part == "10" or part == "55":
    unitcost = 1.00
elif part == "99":
    unitcost = 2.00
elif part == "80" or part == "70":
    unitcost = 3.00
else:
    unitcost = 5.00

#Compute total cost
totalcost = quantity * unitcost

#Display results 
print("\n{:<15} {:>12}".format("Part Number", part))
print("{:<15} ${:>11.2f}".format("Unit Cost", unitcost))
print("{:<15} ${:>11.2f}".format("Total Cost", totalcost))

