master_name = "Diego"
student_name = input("Whats your student name:\n").capitalize()
student_age = int(input("How old are you:\n"))
acces_granted = True if student_name==master_name or student_age>=18 else False

if not acces_granted:
    print("You dont meet the conditions for entry, sorry")
    exit()
print(f"Welcome {student_name.upper()}: {student_age} years old\n")

def enumerate_iterable(iterable):
    if isinstance(iterable, dict):
        for position, (keyword, item_contained) in enumerate(iterable.items(), start = 1):
            print(f"{position}) {keyword}: {item_contained} ")
    else:
        for position, item_contained in enumerate(iterable, start = 1):
            print(f"{position}) {item_contained} ")

stock = {
    "Gold": 9,
    "Iron": 13,
    "Uranium": 4,
    "Plutonium": 6
}

alchemy_laws = (
    "No experimentation with humans",
    "Do Not Create Gold"
    "Respect the Master"
)

print("What 5 materials do you want to introduce to the stock?:")
limit = 0
enumerate_iterable(stock)

while True:
    new = input("").capitalize()
    if new in stock.keys():
        stock[new] += 1
    else:
        stock[new] = 1
    limit += 1
    print("  -----------  ")
    enumerate_iterable(stock)
    print("  -----------  ")
    if limit == 5:
        break