class Vehicle:
    def __init__(self, brand, model, rental_rate):
        self.brand = brand
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Rental Rate: ${self.rental_rate}/day")


class Car(Vehicle):
    def __init__(self, brand, model, rental_rate):
        super().__init__(brand, model, rental_rate)

    def open_trunk(self):
        print(f"{self.brand} {self.model}: Trunk opened.")


class Bike(Vehicle):
    def __init__(self, brand, model, rental_rate):
        super().__init__(brand, model, rental_rate)

    def kickstart(self):
        print(f"{self.brand} {self.model}: Bike kickstarted.")


class LuxuryFeatures:
    def enable_gps(self):
        print("GPS enabled.")

    def enable_heated_seats(self):
        print("Heated seats enabled.")


class LuxuryCar(Car, LuxuryFeatures):
    def __init__(self, brand, model, rental_rate, luxury_charge):
        super().__init__(brand, model, rental_rate)
        self.luxury_charge = luxury_charge

    def calculate_rental(self, days):
        base_rental = super().calculate_rental(days)
        return base_rental + (self.luxury_charge * days)

    def display_details(self):
        super().display_details()
        print(f"Luxury Charge: ${self.luxury_charge}/day")



if __name__ == "__main__":
    regular_car = Car("Toyota", "Corolla", 50)
    print("Regular Car Details:")
    regular_car.display_details()
    print(f"Total Rental for 5 days: ${regular_car.calculate_rental(5)}")
    regular_car.open_trunk()
    print()

    
    bike = Bike("Harley-Davidson", "Street 750", 30)
    print("Bike Details:")
    bike.display_details()
    print(f"Total Rental for 3 days: ${bike.calculate_rental(3)}")
    bike.kickstart()
    print()

    
    luxury_car = LuxuryCar("Mercedes", "S-Class", 200, 50)
    print("Luxury Car Details:")
    luxury_car.display_details()
    print(f"Total Rental for 7 days: ${luxury_car.calculate_rental(7)}")
    luxury_car.open_trunk()
    luxury_car.enable_gps()
    luxury_car.enable_heated_seats()