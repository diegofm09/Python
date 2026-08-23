class Car:
    def __init__(self, brand, model, year, price, on_stock):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.on_stock = on_stock

    def drive(self):
        print(f"You are driving the {self.brand} {self.model}")

    def park(self):
        print(f"You have parked the {self.brand} {self.model}")

    def add_discount(self, discount):
        self.price -= discount