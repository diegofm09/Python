from abc import ABC, abstractmethod

class Filter(ABC):
    @abstractmethod
    def apply(self):
        pass

class BlackWhite(Filter):
    def apply(self):
        print("Converted to black and white")

class Orange(Filter):
    def apply(self):
        print("Converted to orange tones")


class ImageEditor:

    def __init__(self, filter):
        self.filter = filter

    def apply_filter(self):
        self.filter.apply()

