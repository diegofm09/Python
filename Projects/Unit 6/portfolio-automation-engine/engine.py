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

def filter_prices(prices_list, cheap_price):
    cheap_stocks = list(filter(lambda x: x["price"] < cheap_price, prices_list))
    return cheap_stocks

def sort_prices(prices_list):
    sorted_stocks = sorted(prices_list, key= lambda x: x["price"], reverse=True)
    return sorted_stocks

def apply_taxes(prices_list):
    try:
        assert prices_list,("The list is empty")
        final_prices = list(map(lambda x: {**x, "price": round(x["price"] * 0.99, 3)}, prices_list))
        return final_prices
    except AssertionError as e:
        print(e)
    except Exception:
        print("Unknown error ocurred")