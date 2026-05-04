def decoration(function):
    def wrapper():
        print("Im about to execute the function")
        function()
        print("The function has finished")
    return wrapper

@decoration
def saludo():
    print("Hi")

saludo()


def get_name(function):
    def wrapper(*args):
        print(f"The function that is going to execute is {function.__name__}")
        function(*args)
    return wrapper

@get_name
def age(age):
    print(f"You are {age} years old")

age(19)


def twice(function):
    def wrapper(*args):
        function(*args)
        function(*args)
    return wrapper

@twice
def fav_color(color):
    print(f"The {color} is so pretty")

fav_color("Red")
