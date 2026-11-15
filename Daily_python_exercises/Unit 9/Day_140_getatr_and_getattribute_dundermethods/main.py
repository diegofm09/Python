
class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __getattribute__(self, name):
        print(f"Searching for {name} attribute...")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print(f"Error, this object has no {name} attribute")
        return None

fruit1 = Fruit("Apple", 23)

print(fruit1.weight)
print(fruit1.color)