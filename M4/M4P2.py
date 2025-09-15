#For pacing
import time

#Greet the user
print("Welcome to the Stock Value Change Calculator!")
time.sleep(1.5)
print("-" * 50)

#Step by step explanation on what the user will do
print("Enter the purchase price per share, the current stock price, and the quantity of shares you own.")
time.sleep(2)
print("Let's calculate how much your stock has increased or decreased in value.")
time.sleep(2)
print("-" * 50)

#Get user input
purchase_price = float(input("Enter the purchase price per share: $"))
current_price = float(input("Enter the current stock price: $"))
quantity = float(input("Enter the quantity of shares you own: "))
print("-" * 50)

#Perform calculation
print("Calculating your stock value change...")
time.sleep(2)
print("Loading...")
time.sleep(2)
print("-" * 50)
value_change = (current_price - purchase_price) * quantity

#Display result
print(f"Value change: ${value_change:.2f}")
if value_change > 0:
    print("Great! Your stock has increased in value.")
elif value_change < 0:
    print("Unfortunately, your stock has decreased in value.")
else:
    print("No change in value. You're breaking even.")
print("-" * 50)
print("Thanks for using the Stock Value Change Calculator! ")
