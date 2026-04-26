import random

print(f"Here is a random number between 0 and 1:\n{random.random()}")
while True:
    choice = input("Do you want to see another? Y or N\n")
    if choice.capitalize() == "Y":
        print(random.random())
    else:
        break

num1 = float(input("Tell me two numbers\n"))
num2 = float(input(""))
print(f"Here is a random number between {num1} and {num2}:\n{random.uniform(num1, num2)}")
while True:
    choice = input("Do you want to see another? Y or N\n")
    if choice.capitalize() == "Y":
        print(random.uniform(num1, num2))
    else:
        break


num1 = float(input("Tell me two numbers\n"))
num2 = float(input(""))
print(f"Here is a random number between {num1} and {num2}:\n{random.randint(num1, num2)}")
while True:
    choice = input("Do you want to see another? Y or N\n")
    if choice.capitalize() == "Y":
        print(random.randint(num1, num2))
    else:
        break