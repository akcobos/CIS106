from program_functions import calculate_discount

#Summary variables
total_quantity = 0
total_discount = 0
total_discounted_price = 0
entry_count = 0

#Loop
answer = input("Would you like to enter purchase data? Enter Yes to continue: ")

while answer.lower() == "yes":
    #Get user input
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    discount_rate = float(input("Enter discount rate (e.g., 0.10 for 10%): "))

    #Call function
    discount_amount, discounted_price = calculate_discount(quantity, price, discount_rate)

    #Display results
    print("\n\tDiscount Summary")
    print("-" * 40)
    print(f"{'Quantity:':<31} {quantity}")
    print(f"{'Price per item:':<25} ${price:>10.2f}")
    print(f"{'Discount amount:':<25} ${discount_amount:>10.2f}")
    print(f"{'Discounted total price:':<25} ${discounted_price:>10.2f}")
    print("-" * 40)

    #summary in loop
    total_quantity += quantity
    total_discount += discount_amount
    total_discounted_price += discounted_price
    entry_count += 1

    answer = input("\nWould you like to enter another purchase? Enter Yes to continue: ")

print("\n\tSummary of All Purchases")
print("-" * 40)
print(f"{'Total entries:':<25}{entry_count:>15.2f}")
print(f"{'Total quantity:':<25}{total_quantity:>15.2f}")
print(f"{'Total discount:':<25}{f'$ {total_discount:,.2f}':>15}")
print(f"{'Total discounted price:':<25}{f'$ {total_discounted_price:,.2f}':>15}")
print("-" * 40)

