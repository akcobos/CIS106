#problem 1
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee: {self.name}")
        print(f"Salary: ${self.salary:,.2f}")

    def compute_bonus(self, rate):
        return self.salary * rate



#problem 2
class Student:
    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.credits = credits

    def compute_tuition(self):
        if self.district_code.upper() == "I":
            return self.credits * 250.00
        else:
            return self.credits * 500.00

    def display_info(self):
        print(f"Student: {self.first_name} {self.last_name}")
        print(f"District Code: {self.district_code}")
        print(f"Credits: {self.credits}")


#problem 3
class StudentWithDC:
    tuition_rates = {
        "I": 250.00,
        "O": 500.00,
        "X": 800.00,
        "G": 250.00
    }

    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.credits = credits

    def compute_tuition(self):
        rate = StudentWithDC.tuition_rates.get(self.district_code, 500.00)
        return self.credits * rate

    def display_info(self):
        print(f"Student: {self.first_name} {self.last_name}")
        print(f"District Code: {self.district_code}")
        print(f"Credits: {self.credits}")
