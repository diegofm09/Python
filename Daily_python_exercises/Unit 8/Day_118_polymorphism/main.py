from abc import ABC, abstractmethod


print("Polymorphism exists when different classes share a method with the same name, allowing us to call it without caring about the specific class type")

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Guau, Guau")

class Cat(Animal):

    def sound(self):
        print("Miaauuu")
        
animals = [Cat(), Dog()]

for animal in animals:
    animal.sound()

print("Since we can use the 'sound()' method in both Cat and Dog, they have polymorphism in sound()")

