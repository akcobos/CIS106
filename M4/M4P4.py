import time

#Greet the user
print("Welcome to the Pedometer Calculator!")
time.sleep(1.5)
print("-" * 50)

#Get user input
first_name = input("Enter your first name: ")
steps_walked = float(input("Enter the number of steps you walked today: "))
print("-" * 50)

#Compute calories burned
print("Calculating calories burned...")
time.sleep(2)
print("Loading...")
time.sleep(1.5)
print("-" * 50)
calories_burned = steps_walked * 0.25

#Display result
print(f"{first_name}, you burned approximately {calories_burned:.2f} calories today!")
print("-" * 50)
print("Keep moving and stay healthy!")
