from car import Car

car1 = Car("Ferrari", "LaFerrari", 2016, 2000000, False)
car2 = Car("Ford", "Mustang", 1999, 76000, True)
car1.drive()
car2.park()
print(car2.price)
car2.add_discount(20000)
print(car2.price)