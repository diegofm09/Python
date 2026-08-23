class Console:
    def __init__(self, brand, year, price, model, for_sale):
        self.brand = brand
        self.year = year
        self.price = price
        self.model = model
        self.for_sale = for_sale
        self.reviewed = False


console_1 = Console("PlayStation", 2022, 550, "PS5", True)

print(console_1.brand)
print(console_1.reviewed)
console_1.reviewed = True
print(console_1.reviewed)
