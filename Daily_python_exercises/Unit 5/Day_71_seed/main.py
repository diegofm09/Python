import random

random.seed(1)
for i in range(5):
    print(random.randint(1,100))
print("\n")

random.seed("hi")
for i in range(5):
    print(random.randint(1,100))
print("\n")

random.seed(1)
for i in range(5):
    print(random.randint(1,100))
print("\n")

random.seed("hi")
for i in range(5):
    print(random.randint(1,100))