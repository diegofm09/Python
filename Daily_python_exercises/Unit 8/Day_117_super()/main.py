class Shape:

    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f'This shape is {self.color} and is {"filled" if self.filled else "Not filled"}')

class Circle(Shape):

    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"And its radius is {self.radius}")

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width


circle = Circle("blue", True, 9)
circle.describe()