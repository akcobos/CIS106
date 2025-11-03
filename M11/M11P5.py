from program_functions import compute_total_and_tax

#Global variables
total = 0
tax = 0

#Summary
total_all_sales = 0
total_all_tax = 0
entry_count = 0

#Loop 
answer = input("Would you like to enter a sale? Enter Yes to continue: ")

while answer.lower() == "yes":
    quantity = float(input("Enter quantity: "))
    unit_price = float(input("Enter unit price: "))

    compute_total_and_tax(quantity, unit_price)

    print("\n\tSales Tax Report")
    print("-" * 40)
    print(f"{'Quantity:':<25}{quantity:>15.2f}")
    print(f"{'Unit price:':<25}${unit_price:>14.2f}")
    print(f"{'Total:':<25}${total:>14.2f}")
    print(f"{'Tax (7%):':<25}${tax:>14.2f}")
    print("-" * 40)

    total_all_sales += total
    total_all_tax += tax
    entry_count += 1

    answer = input("\nWould you like to enter another sale? Enter Yes to continue: ")

#Final summary
print("\n\tSummary of All Sales")
print("-" * 40)
print(f"{'Total entries:':<25}{entry_count:>15.2f}")
print(f"{'Total sales:':<25}${total_all_sales:>14.2f}")
print(f"{'Total tax:':<25}${total_all_tax:>14.2f}")
print("-" * 40)

