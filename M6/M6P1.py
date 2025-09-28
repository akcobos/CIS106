#Input the quantity of widgets
quantity = int(input("Dear user, enter quantity of your widgets: "))
print("-" * 50)

#Determine unit price
if quantity > 10000:
    price = 10.00
elif quantity >= 5000:
    price = 20.00
else:
    price = 30.00

#Compute extended price, tax, and total
extended = quantity * price
tax = extended * 0.07
total = extended + tax

#Display results
print("\nExtended Price:   ${:>12.2f}".format(extended))
print("Tax Amount:       ${:>12.2f}".format(tax))
print("Total:            ${:>12.2f}".format(total))
