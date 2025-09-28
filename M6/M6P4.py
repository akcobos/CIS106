#Input the number of concert tickets
tickets = int(input("Dear user, enter number of concert tickets: "))

#Determine price per ticket based on quantity
if tickets >= 25:
    price = 50.00
elif tickets >= 10:
    price = 60.00
elif tickets >= 5:
    price = 70.00
else:
    price = 75.00

#Compute total cost
total = tickets * price

#Display results
print("-" * 50)
print("\nNumber of Tickets:     {:>10}".format(f"{tickets:,}"))
print("Price Per Ticket:     ${:>10.2f}".format(price))
print("Total Cost:           ${:>10.2f}".format(total))
