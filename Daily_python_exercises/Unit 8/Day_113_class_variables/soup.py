class Soup:

    cutlery = "Spoon"
    num_soups = 0

    def __init__(self, type, price):
        self.type = type
        self.price = price
        Soup.num_soups += 1
        