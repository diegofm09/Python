class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, radius):
        self.radius = radius

class Car:
    def __init__(self, brand, model, horse_power, wheel_radius):
        self.brand = brand
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = Wheel(wheel_radius)

    def describe(self):
        print(f"{self.brand} {self.model} with {self.engine.horse_power}hp and wheels with {self.wheels.radius}cm radius")


car = Car("Porsche", "Turbo GTS", 560, 24)

car.describe()

