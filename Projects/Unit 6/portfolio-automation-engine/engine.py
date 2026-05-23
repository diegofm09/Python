import random

def prices_generator(names, days):
    try:
        assert isinstance(names, tuple), ("Error, you must enter a tuple")
        stocks = []
        for name in names:
            new_stock = {"name": name, "price": 100}
            stocks.append(new_stock)
        yield stocks

        for i in range (1,days):
            for stock in stocks:
                stock["price"] *= random.uniform(0.94, 1.06)
                stock["price"] = round(stock["price"], 3)
            yield stocks      
    except AssertionError as e:
        print(e)
    except Exception:
        print("Unknown error")

