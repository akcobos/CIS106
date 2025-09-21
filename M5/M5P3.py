#Delay messages for easy flow. Source: https://www.geeksforgeeks.org/python/python-time-module/
import time

#Greet the user
print ("Dear client, thank you for using my Cost Per Book Calculator!")
print ("-" * 50)
time.sleep (2)

#Get user input
books = int(input("Enter the number of books you will order :"))
cost = float(input("Now enter the cost per book :"))
print("-" * 50)

#Determine total cost 
cost = books * cost

#Determine shipping charge
if cost > 50.00:
    shipping = 0.00
else:
    shipping = 25.00
if shipping == 0.00:
    print("You get free shipping!")    

#Compute the order's final total including shipping
total = cost + shipping

#Display results
print("\nBook Cost:                ${:.2f}" .format(cost))
print("Shipping Charge:          ${:.2f}" .format(shipping))
print("Order Total:              ${:.2f}" .format(total))

#Goodbye message
print("-" * 50)
print("Thank you for using the Cost Per Book Calculator! Enjoy!")
