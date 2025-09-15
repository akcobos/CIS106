#add time when delaying a message 
import time
#Greeting
print("Welcome to the Meal Tip Calculator!")
print("-" * 50)

#Get user input
meal_total = float(input("Enter the total cost of your meal: $"))
print("-" * 50)
print("Calculating tip options...")
time.sleep(2)
print("Loading...")
time.sleep(2)
print("-" * 50)

#Tip percentages
tip_rates = [0.15, 0.18, 0.20]

#Display formatted output for each tip rate
for rate in tip_rates:
    tip_amount = meal_total * rate
    total_with_tip = meal_total + tip_amount

    print(f"With {int(rate * 100)}% Tip:")
    print()  # Blank line after the label
    print(f"Total:             {meal_total:>6.2f}")
    print(f"Tip:               {tip_amount:>6.2f}")
    print(f"Total with Tip:    {total_with_tip:>6.2f}")
    print()  # Blank line between each set
