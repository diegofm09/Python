import engine
import utils
import time
import datetime

while True:
    match selection:=input("Menu:\n 1)Run simulation\n 2)View Global analytics\n 3)Exit\n"):
        case "1":
            stocks_names = ("NDX", "AAPL", "MSFT", "NYSE")
            @utils.show_time
            def simulate():
                while True:
                    try:
                        initial_capital = int(input("Enter your initial capital:\n"))

                        while True:
                            start_date = input("Enter your start date:\n")
                            if isinstance(utils.date_validator(start_date), datetime.date):
                                start_date = utils.date_validator(start_date)
                                break

                        users_days = int(input("Enter the amount of days you want to simulate:\n"))

                        for day, prices in enumerate(engine.prices_generator(stocks_names, users_days)):
                            print(f"-- Day {day}:  --")
                            #Hacer que aparezca aqui tambien la fecha de cada dia segun pasan
                            for x in prices:
                                print(f"- {x['name']}: {x['price']}")

                    except ValueError:
                        print("Error, you must enter a number for the initial capital and the number of days")


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