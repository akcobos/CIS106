#Compute miles per gallon
def compute_mpg(miles, gallons):
    if gallons == 0:
        return 0.0  
    return miles / gallons

#Begin trip counter
trip_count = 0

#Loop
answer = input("Would you like to enter a trip? Enter Yes to continue: ")

while answer.lower() == "yes":
    #Get trip data
    city = input("Enter destination city: ")
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))

    #Compute MPG
    mpg = compute_mpg(miles, gallons)

    #Display trip info
    print("\n{:<20} {:>10} {:>10}".format("Destination", "Miles", "MPG"))
    print("-" * 40)
    print("{:<20} {:>10.1f} {:>10.2f}".format(city, miles, mpg))
    print("-" * 40)

    #Increment trip count
    trip_count += 1

    #Ask to continue
    answer = input("\nWould you like to enter another trip? Enter Yes to continue: ")

#Final output
print("\nTotal Trips Entered: {}".format(trip_count))
