#Get user input
principal = float(input("Enter principal amount: $"))
rate = float(input("Enter interest rate (as a decimal, e.g. 0.10 for 10%): "))

#Set total interest
total_interest = 0.0

#Header
print("\nYear\t  Beginning\t  Ending")
print("    \t  Balance  \t  Balance")

#Loop for 5 years
for year in range(1, 6):
    beginning_balance = principal
    interest = beginning_balance * rate
    ending_balance = beginning_balance + interest
    total_interest += interest

    #Format year, beginning, and ending balances
    print(f"{year}\t${beginning_balance:10,.2f}\t${ending_balance:10,.2f}")

    #Update principal for next year
    principal = ending_balance

#Display total interest earned
print(f"\nTotal interest earned: ${total_interest:,.2f}")

