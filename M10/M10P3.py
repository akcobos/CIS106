from program_functions import out_the_door_price
total_msrp = 0
total_final_price = 0
car_count = 0

#Loop
answer = input("Would you like to enter car data? Enter Yes to continue: ")

while answer.lower() == "yes":
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    ev_code = input("Is this an electric vehicle? (Y/N): ")
    msrp = float(input("Enter MSRP (sticker price): "))

    #Compute final price
    final_price = out_the_door_price(make, model, ev_code, msrp)

    #Display results
    print("\nAutomobile Price Estimate")
    print("-" * 40)
    print(f"{'Original MSRP:':<30} ${msrp:>10,.2f}")
    print(f"{'Final price (with tax):':<30} ${final_price:>10,.2f}")
    print("-" * 40)
    total_msrp += msrp
    total_final_price += final_price
    car_count += 1

    answer = input("\nWould you like to enter another car? Enter Yes to continue: ")

#Final summary 
print("\nSummary of All Cars")
print("-" * 40)
print(f"{'Total cars entered:':<30} {car_count:>10}")
print(f"{'Total MSRP:':<30} ${total_msrp:>10,.2f}")
print(f"{'Total final price:':<30} ${total_final_price:>10,.2f}")
print("-" * 40)

