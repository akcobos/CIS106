#Problem 1
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"{'Employee:':<15}{self.name}")
        print(f"{'Salary:':<15}${self.salary:,.2f}")

    def compute_bonus(self, rate):
        return self.salary * rate


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def long_term_bonus(self):
        return self.salary * 0.40


#Problem 2
class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        return self.sticker_price * 0.90

    def display_info(self):
        print(f"{'Make:':<15}{self.make}")
        print(f"{'Model:':<15}{self.model}")
        print(f"{'Sticker Price:':<15}${self.sticker_price:,.2f}")
        print(f"{'Discount Price:':<15}${self.discount_price():,.2f}")


class Sportcar(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = "N"
        self.sport_engine = "N"
        self.sport_interior = "N"

    def set_sport_wheels(self, option):
        self.sport_wheels = option

    def set_sport_engine(self, option):
        self.sport_engine = option

    def set_sport_interior(self, option):
        self.sport_interior = option

    def updated_price(self):
        price = self.discount_price()
        if self.sport_wheels.upper() == "Y":
            price += 1000.00
        if self.sport_engine.upper() == "Y":
            price += 3000.00
        if self.sport_interior.upper() == "Y":
            price += 2000.00
        return price

    def display_info(self):
        print(f"{'Make:':<15}{self.make}")
        print(f"{'Model:':<15}{self.model}")
        print(f"{'Sticker Price:':<15}${self.sticker_price:,.2f}")
        print(f"{'Discount Price:':<15}${self.discount_price():,.2f}")
        print(f"{'Updated Price:':<15}${self.updated_price():,.2f}")
