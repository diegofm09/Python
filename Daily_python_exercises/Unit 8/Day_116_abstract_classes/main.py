from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, type):
        self.type = type

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Cow(Animal):

    def eat(self):
        print("This cow is eating")

    def sleep(self):
        print("This cow is sleeping")

    def name(self):
        print("Hi i am a cow")

cow = Cow("Mammal")
cow.name()

class Lion(Animal):

    def eat(self):
        print("This lion is eating")

    def sleep(self):
        print("This lion is sleeping")