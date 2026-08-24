from plant import Plant

class AppelTree(Plant):

    def __init__(self, apple_color, apple_price):
        self.apple_color = apple_color
        self.apple_price = apple_price

    def take_apple(self):
        print("You have taken an apple")
        

apple_tree_1 = AppelTree("Red", 1)


