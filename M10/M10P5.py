from program_functions import assessed_value

total_market_value = 0
total_assessed_value = 0
home_count = 0

#Loop 
answer = input("Would you like to enter home data? Enter Yes to continue: ")

while answer.lower() == "yes":
    county = input("Enter county name: ")
    market_value = float(input("Enter market value of the home: "))

    #Compute assessed value
    value = assessed_value(county, market_value)

    #Display results
    print("\nHome Assessment Estimate")
    print("-" * 40)
    print(f"{'County:':<30} {county}")
    print(f"{'Market value:':<30} ${market_value:>10,.2f}")
    print(f"{'Assessed value:':<30} ${value:>10,.2f}")
    print("-" * 40)

    total_market_value += market_value
    total_assessed_value += value
    home_count += 1

    answer = input("\nWould you like to enter another home? Enter Yes to continue: ")

#Final summary
print("\nSummary of All Homes")
print("-" * 40)
print(f"{'Total homes entered:':<30} {home_count:>10}")
print(f"{'Total market value:':<30} ${total_market_value:>10,.2f}")
print(f"{'Total assessed value:':<30} ${total_assessed_value:>10,.2f}")
print("-" * 40)
