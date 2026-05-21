def process_purchase():
    if (cost:= input("How much it cost")) == "":
        raise ValueError("It had to cost something")
    cost = float(cost)
    assert cost > 1, ("It had to cost more than 0")

try:
    process_purchase()
except ValueError as ex:
    print("Error with the cost typing")
    print(ex)
except AssertionError:
    print("Error, it had to cost more than 0")
