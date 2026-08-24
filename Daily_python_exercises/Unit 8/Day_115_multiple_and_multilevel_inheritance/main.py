class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is running away")

class Mouse(Prey):
    pass

mouse = Mouse("Mickey")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Lion(Predator):
    pass

class Snake(Prey, Predator):
    pass


lion = Lion("Howey")
snake = Snake("Siss")

mouse.flee()
lion.hunt()
print("\n")
snake.flee()
snake.hunt()

snake.eat()