#Input the principal and years to maturity
principal = float(input("Dear user, enter principal amount: $"))
years = int(input("Now enter years to maturity: "))
print("-" * 50)

#Determine interest rate
if principal > 100000 and years == 5:
    rate = 0.06
elif 50000 <= principal <= 100000 and years == 10:
    rate = 0.05
elif 50000 <= principal <= 100000 and years == 5:
    rate = 0.04
else:
    rate = 0.02

#Compute first year interest
interest = principal * rate

#Display results with aligned decimals
print("\n{:<20} ${:>12.2f}".format("Principal", principal))
print("{:<20} {:>13.2f}%".format("Interest Rate", rate * 100))
print("{:<20} ${:>12.2f}".format("First Year Interest", interest))
