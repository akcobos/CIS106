from classes import Employee

def main():
    emp = Employee(
        "Alice Frost",
        60000
    )

    emp.display_info()

    rate = float(input("Enter bonus rate (e.g., 0.10 for 10%): "))
    bonus = emp.compute_bonus(rate)
    print(f"Bonus: ${bonus:,.2f}")

if __name__ == "__main__":
    main()



