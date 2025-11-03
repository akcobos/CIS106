from program_functions import compute_sales_metrics

#Summary variables
total_sales = 0
total_commission = 0
total_targets = 0
entry_count = 0

#Loop
answer = input("Would you like to enter sales data? Enter Yes to continue: ")

while answer.lower() == "yes":
    last_name = input("Enter salesperson's last name: ")
    sales = float(input("Enter total sales: "))

    commission, next_year_target = compute_sales_metrics(sales)

    print("\n\tSales Report")
    print("-" * 40)
    print(f"{'Salesperson:':<31} {last_name}")
    print(f"{'Total sales:':<25} ${sales:>10.2f}")
    print(f"{'Commission earned:':<25} ${commission:>10.2f}")
    print(f"{'Next year target:':<25} ${next_year_target:>10.2f}")
    print("-" * 40)

    total_sales += sales
    total_commission += commission
    total_targets += next_year_target
    entry_count += 1

    answer = input("\nWould you like to enter another salesperson? Enter Yes to continue: ")

#Final summary
print("\n\tSummary of All Sales")
print("-" * 40)
print(f"{'Total entries:':<25}{entry_count:>15.2f}")
print(f"{'Total sales:':<25}{f'$ {total_sales:,.2f}':>15}")
print(f"{'Total commission:':<25}{f'$ {total_commission:,.2f}':>15}")
print(f"{'Total next year targets:':<25}{f'$ {total_targets:,.2f}':>15}")
print("-" * 40)
