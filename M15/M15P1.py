from classes import Employee, Manager

def main():
    employees = [
        Employee("Kyle Bryant", 60000),
        Employee("Seth Goldberg", 55000)
    ]

    managers = [
        Manager("Diana Nguyen", 80000),
        Manager("Artem Kelman", 95000)
    ]

    print(f"{'Name':<20}{'Salary':>12}{'Bonus':>12}{'Long-Term Bonus':>18}")
    print("-" * 64)

    for emp in employees:
        print(f"{emp.name:<20}{emp.salary:>12,.2f}{emp.compute_bonus(0.10):>12,.2f}{'N/A':>18}")

    for mgr in managers:
        print(f"{mgr.name:<20}{mgr.salary:>12,.2f}{mgr.compute_bonus(0.10):>12,.2f}{mgr.long_term_bonus():>18,.2f}")

if __name__ == "__main__":
    main()
