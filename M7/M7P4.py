#Begin program
count = 0
totalpay = 0
#Ask user if they'd like to start the program
answer = input("Would you like to run the program? Enter Yes to continue: ")
print("-" * 60)

#Loop control
while answer == "Yes" or answer == "yes":
    #Input employee data
    lastname = input("Enter employee last name: ")
    hours = float(input("Enter hours worked: "))
    payrate = float(input("Enter rate of pay: "))

    #Calculate gross pay

    if hours > 40:
        grosspay = 40 * payrate + (hours - 40) * payrate * 1.5
    else:
        grosspay = hours * payrate

    #Update totals    

    totalpay = totalpay + grosspay
    count = count + 1
    print("-" * 60)

    #Display employee information
    print("{:<20} {:>12}".format("Employee", "Gross Pay"))
    print("{:<20} {:>12}".format(lastname, f"${grosspay:,.2f}"))

    #Prompt user once again inside the loop
    answer = input("Would you like to run the program again? Enter Yes to continue: ")
    print("-" * 60)

#After loop is done
if count > 0:
    averagepay = totalpay / count
    print("\n{:<22} {:>12}".format("Total Gross Pay:", f"${totalpay:,.2f}"))
    print("{:<22} {:>12}".format("Average Pay:", f"${averagepay:,.2f}"))
    print("{:<22} {:>12}".format("Number of Employees:", count))
else:
    print("\nNo employee data was entered.")
