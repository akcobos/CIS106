from classes import Student

def main():
    stu = Student(
        "Kyle",
        "Bryant",
        "I",
        12
    )

    print(f"{'Student':<20}{'District':<10}{'Credits':<10}{'Tuition Owed':>15}")
    print("-" * 55)

    print(f"{stu.first_name + ' ' + stu.last_name:<20}{stu.district_code:<10}{stu.credits:<10}{stu.compute_tuition():>15,.2f}")

if __name__ == "__main__":
    main()
