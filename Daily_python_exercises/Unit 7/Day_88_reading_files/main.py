file = open("Daily_python_exercises/Unit 7/Day_88_file_handling/fruit_list.txt", "r")

fruits = (file.read())

file.close()

print(f"Raw string:\n{repr(fruits)}")
fruits = sorted(fruits.split("\n"))

for fruit in fruits:
    print(f"- {fruit.capitalize()}")