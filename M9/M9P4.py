#Determine pay rate based on job code using this function
def get_pay_rate(job_code):
    job_code = job_code.upper()
    if job_code == "L":
        return 25.0
    elif job_code == "A":
        return 30.0
    elif job_code == "J":
        return 50.0
    else:
        return 0.0  

#Begin totals
total_gross_pay = 0
employee_count = 0

#Loop
answer = input("Would you like to enter employee data? Enter Yes to continue: ")

while answer.lower() == "yes":
    #Get employee data
    lastname = input("Enter employee last name: ")
    job_code = input("Enter job code (L, A, J): ")
    hours = float(input("Enter hours worked: "))

    #Get pay rate from function
    rate = get_pay_rate(job_code)

    #Compute gross pay with overtime
    if hours > 40:
        gross_pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        gross_pay = hours * rate

    #Display employee info
    print("\n{:<15} {:>15}".format("Employee", "Gross Pay"))
    print("-" * 30)
    print("{:<15} {:>15}".format(lastname, f"${gross_pay:,.2f}"))
    print("-" * 30)

    #Update totals
    total_gross_pay += gross_pay
    employee_count += 1

    #Ask to continue
    answer = input("\nWould you like to enter another employee? Enter Yes to continue: ")

#Final output
print("\n{:<25} {:>12}".format("Total Gross Pay:", f"${total_gross_pay:,.2f}"))
print("{:<25} {:>12}".format("Employees Entered:", employee_count))

