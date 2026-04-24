import math

radius = float(input("Whats the circunference radius:\n"))

circunference = 2*math.pi*radius
print(f"The circunference is {round(circunference, 3)}")

area = math.pi*radius**2
print(f"The area is {round(area, 3)}")

side_a = float(input("How much cm is the 'a' side\n"))
side_b = float(input("How much cm is the 'b' side\n"))
side_c = math.sqrt(side_a**2 + side_b**2)
print(f"The side 'c' is {side_c} cm")