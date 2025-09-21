#Use to pace messages for readability. Source: https://www.geeksforgeeks.org/python/python-time-module/

import time

#Greet the user
print("Welcome to the Quantity Pricing Calculator!")
time.sleep(1.5)
print("-" * 50)

#Get user input
quantity = int(input("Please enter the quantity of items: "))
print("-" * 50)

#Compute unit price
print("Calculating pricing details...")
time.sleep(2)
print("...")
time.sleep(1.5)
print("-" * 50)
if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

#Compute extended price, tax, and total
extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax

#Display results
print(f"Quantity:         {quantity}")
print(f"Unit Price:       ${unit_price:.2f}")
print(f"Extended Price:   ${extended_price:.2f}")
print(f"Tax (7%):         ${tax:.2f}")
print(f"Total:            ${total:.2f}")
print("-" * 50)
print("Thank you for using the calculator!")

