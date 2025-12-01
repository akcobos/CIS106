from classes import Car, Sportcar

def main():
    cars = [
        Car("Toyota", "Camry", 30000),
        Car("Honda", "Accord", 28000)
    ]

    sportcars = [
        Sportcar("Ford", "Mustang", 40000),
        Sportcar("Chevy", "Corvette", 60000)
    ]

    sportcars[0].set_sport_wheels("Y")
    sportcars[0].set_sport_engine("N")
    sportcars[0].set_sport_interior("Y")

    sportcars[1].set_sport_wheels("Y")
    sportcars[1].set_sport_engine("Y")
    sportcars[1].set_sport_interior("Y")

    print(f"{'Make':<12}{'Model':<12}{'Sticker':>12}{'Discount':>12}{'Updated':>12}")
    print("-" * 60)

    for car in cars:
        print(f"{car.make:<12}{car.model:<12}{car.sticker_price:>12,.2f}{car.discount_price():>12,.2f}{car.discount_price():>12,.2f}")

    for sportcar in sportcars:
        print(f"{sportcar.make:<12}{sportcar.model:<12}{sportcar.sticker_price:>12,.2f}{sportcar.discount_price():>12,.2f}{sportcar.updated_price():>12,.2f}")

if __name__ == "__main__":
    main()
