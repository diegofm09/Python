class Cow():
    def sound(self):
        print("Muuu")

class Car():
    def sound(self):
        print("Beep Beep")


make_sound = [Car(), Cow()]

for i in make_sound:
    print(i.sound())

print("Both classes are independent from each other and dont share a parent, but they still can both call sound method, they have polymorphism")