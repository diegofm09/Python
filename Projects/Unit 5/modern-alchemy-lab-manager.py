logs = []
master_name = "Diego"
student_name = input("Whats your student name:\n").capitalize()
student_age = int(input("How old are you:\n"))
acces_granted = True if student_name==master_name or student_age>=18 else False
logs.append("Entered the system")

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

def add_potion(name, power, *extras, **details):
    global potions
    new_potion = {"name": name, "power": power}
    potions.append(new_potion) 
    print(f"{name.upper()} added sucesfully to potions list:")
    print(f" Power: {power}")
    if extras:
        for i in extras:
            print(f" - Add {i.capitalize()}")
    if details:
        for (x,y) in details.items():
            print(f" - {x.capitalize()}: {y.capitalize()}")

    
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
potions_names = list(map(lambda x: x["name"].upper(), potions))

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
logs.append("Added materials to the stock")

print("Great, entering The Hub")
logs.append("Entered The Hub")
while True: 

    print("  -----------  ")
    the_hub_selection = input("Select an option:\n 1) Inventory\n 2) Alchemy Laws\n 3) Brewing Room\n 4) Laboratory Audit\n 5) Recipe Management\n 6) Exit The Hub\n")
    print("  -----------  ")

    match the_hub_selection:
        case "1":
            print("Stock:")
            enumerate_iterable(stock)
            logs.append("Checked the Stock")

        case "2":
            print("Alchemy Laws:")
            enumerate_iterable(alchemy_laws)
            logs.append("Checked alchemy laws")
    
        case "3":
            logs.append("Entered Brewing Room")
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
                            logs.append("Massive Transmutation")
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
                            logs.append("Energy Creation")

                    case "3":
                        print("Laboratory state:")
                        print("SAFE" if sum(stock.values())%2==0 else "UNSAFE")
                        logs.append("Checked Laboratory state")

                    case "4":
                        print("  -----------  ")
                        print("Exiting Brewing Room")
                        logs.append("Exited Brewing Room")
                        break

        case "4":
            logs.append("Watched global report")
            print("GLOBAL REPORT:")
            print(f" The Stock has a total of {sum(stock.values())} units")
            print(f" The material with higher Stock is the {max(stock, key=stock.get)}")
            print(f" You are {student_name}")
            print(f" Last 2 operations done: {logs[-2:]}")
            entire_log_selection = input("Do you want to see the whole logs\n 1) Yes\n 2) No\n")
            match entire_log_selection:
                case "1":
                    print("Logs of the sesion:")
                    enumerate_iterable(logs)
                    logs.append("Watched whole logs")

                case "2":
                    print("Ok")

                case _:
                    print("Error, enter 1 or 2")


        case "5":
            logs.append("Entered Recipe Managment")
            print("Entering Recipe Managment:")
            while True:
                print("  -----------  ")
                recipe_managment_selection = input("Recipe Managment:\n Select an option\n  1) Potions list\n  2) Master Sort\n  3) New Potion\n  4) The Essence Filter\n  5) Exit Recipe Managment\n")
                match recipe_managment_selection:
                    case "1":
                        print("Potions List:")
                        enumerate_iterable(potions)
                        logs.append("Watched Potions List")

                    case "2":
                        print("  -----------  ")
                        print("Sorting Potions...")
                        potions = sorted(potions, key= lambda x: x["power"], reverse=True)
                        enumerate_iterable(potions)
                        logs.append("Sorted Potions")

                    case "3":
                        new_potion_name = input("What do you want to call the new potion:\n")
                        new_potion_power = 0

                        while True:
                            new_potion_power = int(input("What power do you want to give the potion:\n"))
                            new_potion_power = new_potion_power if new_potion_power<500 and new_potion_power>0 else 0
                            if new_potion_power > 0:
                                break
                            else:
                                print("Error, the potion power must be between 0 and 500")

                        new_potion_extra_materials = []
                        while True:
                            extra_material_selection = input("Do you want to add some special material to the potion?\n 1) Yes\n 2) No\n")
                            match extra_material_selection:
                                case "1":
                                    new_potion_extra_materials.append(input("What material do you want to add\n"))
                                case "2":
                                    break
                                case _:
                                    print("Error, please enter either 1 or 2")
                        print("  -----------  ")

                        new_potion_details = {}
                        while True:
                            detail_selection = input("Do you want to specify some details of the potion?\n 1) Yes\n 2) No\n")
                            match detail_selection:
                                case "1":
                                    new_potion_details_key = input("What do you want to specify?\n  Example --> Color, temperature...\n")
                                    new_potion_details_value = input("What do you want it to be\n  Example --> Purple, hot...\n")
                                    new_potion_details[new_potion_details_key.capitalize()] = new_potion_details_value.capitalize()
                                case "2":
                                    break
                                case _:
                                    print("Error, please enter either 1 or 2")
                        print("  -----------  ")

                        add_potion(new_potion_name, new_potion_power, *new_potion_extra_materials, **new_potion_details)
                        logs.append("Created a new potion")

                    case "4":
                        print("Potions Names:")
                        enumerate_iterable(potions_names)
                        
                        minimum_power = int(input("What minimum power level do you want to see the potions with:\n"))
                        high_power_potions = filter(lambda x: True if x["power"]>minimum_power else False, potions)
                        enumerate_iterable(high_power_potions)
                        logs.append("Watched potions with a minimum power")

                    case "5":
                        print("  -----------  ")
                        print("Exiting Recipe Managment")
                        logs.append("Exited Recipe Managment")
                        break

        case "6":
            print("Exiting The Hub")
            exit()

        case _:
            print("Error, option not avaiable")
