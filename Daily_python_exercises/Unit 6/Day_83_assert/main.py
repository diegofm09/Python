def start_programme(dictionary):
    assert isinstance(dictionary,dict), "Invalid data type"
    assert dictionary, "Empty dictionary"
    print("Loaded succesfully")

colors = ["Blue", "Red", "Yellow"]
prices = {"IPad": 670, "IPhone": 1200, "TV": 430}
empty = dict({})

if __name__ == "__main__":
    try:
        start_programme(prices)
    except AssertionError:
        print("Error with the data")
    try:
        start_programme(colors)
    except AssertionError:
        print("Error with the data")
    try:
        start_programme(empty)
    except AssertionError:
        print("Error with the data")