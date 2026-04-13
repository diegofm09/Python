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
            if isinstance(item_contained, dict):
                name = item_contained.get("name", "Unknown")
                power = item_contained.get("power", "??")
                print(f"{position}) {name}, Power: {power}")
            else:
                print(f"{position}) {item_contained} ")

def add_energy(energy):
    return energy + 20
    
stock = {
    "Gold": 9,
    "Iron": 13,
    "Uranium": 4,
    "Plutonium": 6,
    "Calcium": 15,
    "Carbon": 10,
}

alchemy_laws = (
    "No experimentation with humans",
    "Do Not Create Gold",
    "Respect the Master",
)

potions = [
    {"name": "Dragon Killer", "power": 120},
    {"name": "Love Shot", "power": 30},
    {"name": "Angelical Water", "power": 75},
    {"name": "Nuclear Posion", "power": 90},
    {"name": "Gods Tears", "power": 150},
    {"name": "Hell Blood", "power": 50},
]
potions_names = [i["name"].upper() for i in potions]

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
massive_transmutation_uses = 0
current_energy = 0
print("Great, entering The Hub")
while True: 

    print("  -----------  ")
    the_hub_selection = input("Select an option:\n 1) Inventory\n 2) Alchemy Laws\n 3) Brewing Room\n 4) Laboratory Audit\n 5) Recipe Management\n 6) Exit The Hub\n")
    print("  -----------  ")

    match the_hub_selection:
        case "1":
            print("Stock:")
            enumerate_iterable(stock)

        case "2":
            print("Alchemy Laws:")
            enumerate_iterable(alchemy_laws)
    
        case "3":
            print("Entering Brewing Room:")
            while True:
                print("  -----------  ")
                brewing_room_selection = input("Brewing Room:\n Select an option\n  1) Massive Transmutation\n  2) Energy Creator\n  3) Safety Check\n  4) Exit Brewing Room\n")
                
                match brewing_room_selection:
                    case "1":
                        if massive_transmutation_uses==0:
                            print("  -----------  ")
                            print("Doing a massive transmutation, result:")
                            stock = {element: cuantity*3 for (element, cuantity) in stock.items()}
                            massive_transmutation_uses = 1
                            enumerate_iterable(stock)
                        else:
                            print("  -----------  ")
                            print("You have already used massive transmutation once")

                    case "2":
                        while True:
                            print(f"Energy Creator:\n Current energy: {current_energy}")
                            energy_creator_selection = input("  Press 1 to add 20 energy\n  Press 2 to exit Energy Creator\n")
                            if energy_creator_selection == "2":
                                break
                            elif energy_creator_selection=="1":
                                if current_energy == 100:
                                    print("  -----------  ")
                                    print("Error, Energy at maximum capacity")
                                else:
                                    current_energy = min(100, add_energy(current_energy))
                                print("  -----------  ")
                            else:
                                print("Error, option not avaiable")
                                print("  -----------  ")

                    case "3":
                        print("Laboratory state:")
                        print("SAFE" if sum(stock.values())%2==0 else "UNSAFE")

                    case "4":
                        print("  -----------  ")
                        print("Exiting Brewing Room")
                        break

        case "4":
            pass

        case "5":
            print("Entering Recipe Managment:")
            while True:
                print("  -----------  ")
                recipe_managment_selection = input("Recipe Managment:\n Select an option\n  1) Potions list\n  2) Master Sort\n  3) New Potion\n  4) The Essence Filter\n  5) Exit Recipe Managment\n")
                match recipe_managment_selection:
                    case "1":
                        print("Potions List:")
                        enumerate_iterable(potions)

                    case "2":
                        print("  -----------  ")
                        print("Sorting Potions...")
                        potions = sorted(potions, key= lambda x: x["power"], reverse=True)
                        enumerate_iterable(potions)

                    case "3":
                        pass

                    case "4":
                        #Hacer estas 2 cosas con higher order functionsw
                        print("Potions Names:")
                        enumerate_iterable(potions_names)
                        
                        minimum_power = int(input("What minimum power level do you want to see the potions with:\n"))
                        high_power_potions = []
                        for potion in potions:
                            if potion["power"]>minimum_power:
                                high_power_potions.append(potion["name"])
                        print(f"Potions with higher power than {minimum_power}:")
                        enumerate_iterable(high_power_potions)

                    case "5":
                        pass

        case "6":
            print("Exiting The Hub")
            exit()

        case _:
            print("Error, option not avaiable")
