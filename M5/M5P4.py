#Delay messages for readability
import time

#Greet the user
print("Greetings! Thank you for using the Appliance Warranty Calculator!")
print("-" * 50)
time.sleep (2)

#Input: appliance name and cost
appliance_name = input("Enter the name of the appliance you'd wish to calculate: ")
cost = float(input("Now enter the cost of the appliance: $"))
print("-" * 50)

#Determine warranty
if cost > 1000.00:
    warranty = cost * 0.10
else:
    warranty = cost * 0.05

#Calculate warranty and total cost
total_cost = cost + warranty

#Display results
print("\nAppliance:         ", appliance_name)
print("Appliance Cost:    ${:.2f}".format(cost))
print("Warranty Cost:     ${:.2f}".format(warranty))
print("Total Cost:        ${:.2f}".format(total_cost))
