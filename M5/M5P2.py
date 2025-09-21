#Get user input for item and quantity
item = input("Dear user, please enter the name of the item: ")
quantity = int(input("Enter the quantity of the item: "))
print("-" *50)

#Compute unit price based on item
if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00

#Calculate extended price
extended_price = quantity * unit_price

#Display results
print("\nItem:            ", item)
print("Unit Price:      ${:.2f}".format(unit_price))
print("Extended Price:  ${:.2f}".format(extended_price))
