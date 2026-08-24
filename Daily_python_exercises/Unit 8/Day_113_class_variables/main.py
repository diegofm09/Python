from soup import Soup

soup1 = Soup("Garlic", 8)
soup2 = Soup("Fish", 9)

print(f"The {soup1.type} costs {soup1.price} and is eaten with {soup1.cutlery}")
print(f"The {soup2.type} costs {soup2.price} and is eaten with {soup2.cutlery}")
print(f"All soups are eaten with {Soup.cutlery}")
print(f"There are {Soup.num_soups} soups")