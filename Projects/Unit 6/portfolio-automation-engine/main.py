import engine
import utils
import time
import datetime

while True:
    match selection:=input("Menu:\n 1)Run simulation\n 2)View Global analytics\n 3)Exit\n"):
        case "1":
            stocks_names = ("NDX", "AAPL", "MSFT", "NYSE", "SPX", "DJI", "VT", "NVDA", "TSLA", "AMD", "JPM", "IWDA", "QQQ")
            one_day = datetime.timedelta(days=1)
            @utils.show_time
            def simulate():
                while True:
                    try:
                        initial_capital = int(input("Enter your initial capital:\n"))

                        while True:
                            start_date = input("Enter your start date:\n")
                            if isinstance(utils.date_validator(start_date), datetime.date):
                                start_date = utils.date_validator(start_date)-one_day
                                break

                        users_days = int(input("Enter the amount of days you want to simulate:\n"))

                        for day, prices in enumerate(engine.prices_generator(stocks_names, users_days)):
                            start_date += one_day
                            print(f"-- Day {day}: {start_date} --")
                            for x in prices:
                                print(f"- {x['name']}: {x['price']}")
                                if day == users_days:
                                    final_prices = [x for x in prices]

                        cheap_price = int(input("What's the minimum stock price you want to filter by?\n"))
                        filtered_prices = engine.filter_prices(final_prices, cheap_price)
                        print(f"-- Sorted and filtered final Stocks:\n  -- All stocks are above {cheap_price}$ --")
                        sorted_prices = engine.sort_prices(filtered_prices)
                        for i in sorted_prices:
                            print(f"  - {i['name']}: {i['price']}")

                        print(f"-- Sorted and filtered final Stocks after taxes:\n  -- The taxes are of 1% of the price --")
                        taxed_prices = engine.apply_taxes(sorted_prices)
                        for i in taxed_prices:
                            profitable = "PROFITABLE" if i["price"]>100 else "LOSS"
                            print(f"  - {i['name']}, final price: {i['price']}, {profitable}")

                        medium_performance = 0
                        counter = 0
                        for x in taxed_prices: 
                            medium_performance+= x["price"]
                            counter += 1
                        medium_performance /= counter
                        final_money = initial_capital*(medium_performance/100)
                        print(f"Your final money is {round(final_money, 4)}$")
                        break
                    except ValueError:
                        print("Error, you must enter a number for prices/money and the number of days")
                    except Exception:
                        print("Unknown error ocurred")


            simulate()
            print("------------")

        case "2":
            print(f"Today {utils.counter} simulations went good")
            print("------------")

        case "3":
            print("Exiting...")
            time.sleep(3)
            print("Program closed")
            exit()

        case _:
            print("Option not available")
            print("------------")