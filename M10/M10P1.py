#import function

from program_functions import compute_forecast 
total_forecasted_sales = 0
forecast_count = 0

#Loop
answer = input("Would you like to enter forecast data? Enter Yes to continue: ")

while answer.lower() == "yes":
    lastname = input("Enter last name: ")
    month = input("Enter current month (e.g., Jan, Feb): ")
    sales = float(input("Enter current sales amount: "))

    next_month_sales = compute_forecast(month, sales)

    print("\n{:<15} {:>20}".format("Employee", "Next Month's Sales"))
    print("-" * 35)
    print("{:<15} {:>20.2f}".format(lastname, next_month_sales))
    print("-" * 35)
    total_forecasted_sales += next_month_sales
    forecast_count += 1

    answer = input("\nWould you like to enter another forecast? Enter Yes to continue: ")

#Final summary
print("\n{:<25} {:>10}".format("Total Forecasts Entered:", forecast_count))
print("{:<25} {:>10.2f}".format("Total Forecasted Sales:", total_forecasted_sales))
