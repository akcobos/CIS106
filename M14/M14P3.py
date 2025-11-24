from classes import StudentWithDC

def main():
    students = [
        StudentWithDC(
            "Seth",
            "Goldberg",
            "I",
            12
        ),
        StudentWithDC(
            "Diana",
            "Nguyen",
            "O",
            15
        ),
        StudentWithDC(
            "Artem",
            "Kelman",
            "X",
            9
        ),
        StudentWithDC(
            "Noor",
            "Nabelsi",
            "G",
            6
        ),
        StudentWithDC(
            "Taylor",
            "Sutter",
            "O",
            10
        )
    ]

    print(f"{'Student':<20}{'District':<10}{'Credits':<10}{'Tuition Owed':>15}")
    print("-" * 55)

    for stu in students:
        print(f"{stu.first_name + ' ' + stu.last_name:<20}{stu.district_code:<10}{stu.credits:<10}{stu.compute_tuition():>15,.2f}")

if __name__ == "__main__":
    main()
