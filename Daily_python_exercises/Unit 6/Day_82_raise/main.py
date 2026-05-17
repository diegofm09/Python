try:
    age = int(input("Enter your age\n"))
    print(f"You are {age} years old")
    if age<0 or age>120:
        raise ValueError("Your age is imposible")
except ValueError as ex:
    print(ex)
    print("Please, enter a non decimal number")
except:
    print("An unknown error ocurred")
