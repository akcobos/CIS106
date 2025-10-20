#Compute extended price with discount
def compute_extended_price(qty, price):
    extended = qty * price
    if extended > 10000:
        extended *= 0.90  #10% discount
    return extended
total_extended_price = 0

#loop
answer = input("Would you like to enter an item? Enter Yes to continue: ")

while answer.lower() == "yes":
    #Get user input
    qty = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    #Compute extended price
    ext_price = compute_extended_price(qty, price)

#Display info
    print("\n{:<10} {:>10} {:>15}".format("Qty", "Price", "Total"))
    print("-" * 35)
    print("{:<10} {:>10} {:>15}".format(qty, f"${price:,.2f}", f"${ext_price:,.2f}"))
    print("\n{:<20} {:>15}".format("Total Extended Price:", f"${total_extended_price:,.2f}"))




    #Add to total
    total_extended_price += ext_price

    #Ask to continue
    answer = input("\nWould you like to enter another item? Enter Yes to continue: ")

#Final output
print("\n{:<22} ${:>10.2f}".format("Total Extended Price:", total_extended_price))
