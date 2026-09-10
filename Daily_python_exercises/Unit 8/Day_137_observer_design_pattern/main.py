from abc import ABC, abstractmethod

class TemperatureSubscriptor(ABC):
    @abstractmethod
    def reload(self, temperature):
        pass

class Screen(TemperatureSubscriptor):
    def reload(self, temperature):
        print(f"Screen: Actual temperature {temperature}C")

class AC(TemperatureSubscriptor):
    def reload(self,temperature):
        if temperature > 25:
            print("AC ON")

class TemperatureSensor:
    def __init__(self):
        self.subscriptors = []

    def new_subscriptor(self, new):
        self.subscriptors.append(new)

    def change_temperature(self,new):
        for i in self.subscriptors:
            i.reload(new)

            