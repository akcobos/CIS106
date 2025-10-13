#Open and read the item data file
with open("orders.txt", "r") as file:
    lines = file.readlines()

#Begin totals
total_price = 0.0
order_count = 0
print(f"{'Item':<10}{'Quantity':>10}{'Price':>10}{'Extended':>15}")
print("-"*50)

#Process each item
for i in range(0, len(lines), 3):
    item = lines[i].strip()
    quantity = int(lines[i + 1].strip())
    price = float(lines[i + 2].strip())

    extended_price = quantity * price
    total_price += extended_price
    order_count += 1

    #Display item info
    print(f"{item:<10}{quantity:>10}{price:>10.2f}{extended_price:>15.2f}")
    print("-"*50)

#Calculate average order
average_order = total_price / order_count if order_count > 0 else 0

#Display summary
print("\nSummary:")
print(f"{'Total extended price:':<25}${total_price:10,.2f}")
print(f"{'Number of orders:':<25}{order_count:>10}")
print(f"{'Average order value:':<25}${average_order:10,.2f}")

