#Begin total discount
sumdiscount = 0

#Prompt before loop
answer = input("Would you like to run the program? Enter Yes to continue: ")
print("-" *65)

#Loop control
while answer == "Yes" or answer == "yes":
    #Input item data
    quantity = int(input("Enter quantity of items: "))
    price = float(input("Enter price per item: "))

    #Compute extended price
    extended = quantity * price

    #Determine discount
    if extended > 10000:
        discount = extended * 0.25
    else:
        discount = extended * 0.10

    #Calculate total and update sum
    total = extended - discount
    sumdiscount += discount
    print("-" * 65)

    #Display results
    print("\n{:<22} ${:>10.2f}".format("Extended Price:", extended))
    print("{:<22} ${:>10.2f}".format("Discount Amount:", discount))
    print("{:<22} ${:>10.2f}".format("Total After Discount:", total))

    #Prompt again inside loop
    answer = input("\nWould you like to run the program again? Enter Yes to continue: ")
    print("-" * 65)

#After loop
print("\n{:<22} ${:>10.2f}".format("Total Discount Given:", sumdiscount))
