import console as c

console_1 = c.Console("PlayStation", 2022, 550, "PS5", True)

print(console_1.brand)
print(console_1.reviewed)
console_1.reviewed = True
print(console_1.reviewed)

console_2 = c.Console("XBox", 2022, 490, "Series X", False)
print(console_2.for_sale)