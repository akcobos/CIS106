import time

#Greeting
print("Welcome to the Break-Even Point Calculator!")
time.sleep(1.5)
print("-" * 50)

#Get user input
fixed_costs = float(input("Enter your fixed costs (in dollars): $"))
price_per_unit = float(input("Enter your selling price per unit: $"))
cost_per_unit = float(input("Enter your cost per unit: $"))
print("-" * 50)

#Compute break-even point
print("Calculating your break-even point...")
time.sleep(2)
print("Crunching the numbers...")
time.sleep(1.5)
print("-" * 50)
profit_per_unit = price_per_unit - cost_per_unit
if profit_per_unit <= 0:
    print("Your price per unit must be greater than your cost per unit to break even.")
else:
    break_even_units = fixed_costs / profit_per_unit
    print(f"To break even, you need to sell approximately {break_even_units:.2f} units.")
    print("-" * 50)
    print("Good luck with your business!")
