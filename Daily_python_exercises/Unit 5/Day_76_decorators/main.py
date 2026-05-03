def add_tomato(function):
    def wrapp(*args):
        print("You added tomato")
        function(*args)
    return wrapp

def add_cheese(function):
    def wrapp(*args):
        print("You added cheese")
        function(*args)
    return wrapp

@add_tomato
@add_cheese
def hamburguer(meat):
    print(f"Here is your {meat} hamburguer")

hamburguer("chicken")