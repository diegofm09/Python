import json

with open("Daily_python_exercises/Unit 7/Day_101_json_introduction/products.json", "r") as file:
    product = json.load(file)

print(f'Product: {product["name"]}\nPrice: {product["price"]}\nIs it in stock?: {product["in_stock"]}')