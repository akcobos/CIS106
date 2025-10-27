from program_functions import ticket_price
total_price = 0
ticket_count = 0

#Loop 
answer = input("Would you like to enter ticket data? Enter Yes to continue: ")

while answer.lower() == "yes":
    last_name = input("Enter passenger's last name: ")
    miles = float(input("Enter miles from downtown Chicago: "))

    #Compute ticket price
    price = ticket_price(miles)

    #Display results 
    print("\nTrain Ticket Estimate")
    print("-" * 40)
    print(f"{'Passenger:':<30} {last_name}")
    print(f"{'Miles from downtown:':<30} {miles:>10.1f}")
    print(f"{'Ticket price:':<30} ${price:>10.2f}")
    print("-" * 40)

    
    total_price += price
    ticket_count += 1

    answer = input("\nWould you like to enter another ticket? Enter Yes to continue: ")

#Final summary
print("\nSummary of All Tickets")
print("-" * 40)
print(f"{'Total tickets sold:':<30} {ticket_count:>10}")
print(f"{'Total ticket revenue:':<30} ${total_price:>10.2f}")
print("-" * 40)
