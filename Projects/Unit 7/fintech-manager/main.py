from core import auth, finance, storage, utils
from pathlib import Path
import json, datetime

main_path = Path(__file__).resolve().parent

config_path = main_path/"config.json"
app_log_path = main_path/"data"/"app_log.txt"
counter = 0

if __name__ == "__main__":
    storage.initialize_files()
    user_name = storage.change_name()
    while True:
        print("  -------------------------")
        selection = input("Menu Selection:\n 1) Profile and balance\n 2) Register Transaction\n 3) Transactions Analysis\n 4) Calculators and Simulators\n 5) Monthly Expenses Analysis\n 6) System Auditory\n 7) Close System\n")
        print("  -------------------------")
        match selection:
            case "1":
                with open(config_path, "r") as file:
                    config = json.load(file)
                trans_list = storage.load_transactions()
                net_balance = finance.analyze_transactions(trans_list)["net_balance"]
                print(f'Profile:\n Username: {user_name}\n Currency: {config["currency"]}\n Expense Limit: {config["expense_limit"]}\n Net Balance: {net_balance}')
                print("✅ ALL GOOD ✅" if net_balance >= 0 else "⚠️ DANGER, NET BALANCE BELOW 0 ⚠️")

            case "2":
                print("New Transaction:")
                amount = float(input("Enter the transaction amount, (If it is an expense, the number must be negative): "))
                evaluate_limit = auth.limit_verif()
                if not evaluate_limit(amount):
                    auth.dinamic_alerts("Error, Expense higher than limit", urgent=True)
                category = input("Enter the number of the category:\n 1) Food \n 2) Job \n 3) Travel \n 4) Subscriptions \n 5) Shopping \n 6) Utilities \n 7) Investments \n 8) Enter 8 if you want to introduce a new personalized category\n")
                match category:
                    case "1":
                        category = "Food"
                    case "2":
                        category = "Job"
                    case "3":
                        category = "Travel"
                    case "4":
                        category = "Subscriptions"
                    case "5":
                        category = "Shopping"
                    case "6":
                        category = "Utilities"
                    case "7":
                        category = "Investments"
                    case "8":
                        category = input("Enter the personalized category: ")
                    case _:
                        print("Error, please enter a number between 1 and 8")
                concept = input("Enter the concept: ")
                date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                id = storage.load_transactions()[-1]["id"] + 1
                print(id)
                print("asw")
                trans_list = storage.load_transactions()
                trans_list.append({"id": id, "amount": amount, "category": category, "concept": concept, "date": date})  
                print(trans_list)
                storage.save_transactions(trans_list)     

            case "3":
                trans_list = storage.load_transactions()
                while True:
                    
                    sub_selection2 = input("Transactions SubMenu:\n 1) Check Transactions\n 2) Analyze Transactions\n 3) Filter Transactions\n 4) Easy Read\n 5) Sort Transactions\n 6) Close SubMenu\n")
                    print("  -------------------------")
                    match sub_selection2:
                        case "1":
                            print("Transactions Check:")
                            if counter == 0:
                                specific_category = input("Do you want to check any specific category?(Y/N): ").capitalize()
                                match specific_category:
                                    case "Y":
                                        specific_category = input("Enter the number of the category:\n 1) Food \n 2) Job \n 3) Travel \n 4) Subscriptions \n 5) Shopping \n 6) Utilities \n 7) Investments \n 8) Enter 8 if you want to introduce a new personalized category\n")
                                        match  specific_category:
                                            case "1":
                                                specific_category = "Food"
                                            case "2":
                                                specific_category = "Job"
                                            case "3":
                                                specific_category = "Travel"
                                            case "4":
                                                specific_category = "Subscriptions"
                                            case "5":
                                                specific_category = "Shopping"
                                            case "6":
                                                specific_category = "Utilities"
                                            case "7":
                                                specific_category = "Investments"
                                            case "8":
                                                specific_category = input("Enter the personalized category: ")
                                            case _:
                                                print("Error, please enter a number between 1 and 8")
                                    case "N":
                                        specific_category = None
                                    case  _:
                                        print("Error, please enter Y or N")

                                data_variable = finance.data_extractor(trans_list, specific_category)

                                add_internationals = input("Do you want to add international movements?(Y/N): ").capitalize()
                                match add_internationals:
                                    case "Y":
                                        counter += 1
                                        generator = next(finance.add_international_movements(data_variable))
                                        print(f'ID: {generator.get("id")} {generator.get("date")}\n  AMOUNT: {generator.get("amount")}$\n  CATEGORY: {generator.get("category")}\n  CONCEPT:{generator.get("concept")}')
                                    case "N":
                                        counter += 1
                                        generator = next(data_variable)
                                        print(f'ID: {generator.get("id")} {generator.get("date")}\n  AMOUNT: {generator.get("amount")}$\n  CATEGORY: {generator.get("category")}\n  CONCEPT:{generator.get("concept")}')
                                 
                                    case  _:
                                        print("Error, please enter Y or N")
                                print("  -------------------------")
                            else:
                                selection = input("Do you want to continue with the previous generator(1) or start a new one(2): ")
                                match selection:
                                    case "1":
                                        print(f'ID: {generator.get("id")} {generator.get("date")}\n  AMOUNT: {generator.get("amount")}$\n  CATEGORY: {generator.get("category")}\n  CONCEPT:{generator.get("concept")}')
                                    case "2":
                                        pass
                                    #TOCA ESTA PRYE---___-d-w-d-we-e-c-edimcoasihfowqufhdiwufhr9uewqhf9ieruhfrwiuoqinndgsyfn
                                    case _:
                                        print("Error, please enter 1 or 2")
                        case "2":
                            print("Transactions Analysis:")
                            analysis = finance.analyze_transactions(trans_list)
                            print(f'Net Balance: {analysis.get("net_balance")}')
                            print(f"Highest Expense: {analysis.get('highest_expense')}")
                            print(f'Highest Income: {analysis.get("highest_income")}')
                            print("  -------------------------")

                        case "3":
                            try:
                                minimum_amount = float(input("Enter the minimum amount to filter by: "))
                                print(f"Transactions with higher amount than {minimum_amount}")
                                for position, i in enumerate(finance.filter_transactions(trans_list, minimum_amount), start = 1):
                                    print(f'{position}) ID:{i[0]} {i[1]}')
                            except ValueError:
                                print("Error, enter a number please")
                            print("  -------------------------")

                        case "4":
                            print("Transactions Easy Read:")
                            easy_read_trans_list = finance.easy_read(trans_list)
                            for i in easy_read_trans_list:
                                print(f"{i}: {easy_read_trans_list[i][0]}, {easy_read_trans_list[i][1]}$")
                            print("  -------------------------")

                        case "5":
                            while True:
                                sort_key = input("Do you want to sort transactions by amount(1) or date(2): ")
                                match sort_key:
                                    case "1":
                                        for position, i in enumerate(finance.sort_transactions(trans_list, "money"), start = 1):
                                            print(f'{position}) ID: {i.get("id")} {i.get("date")}\n  AMOUNT: {i.get("amount")}$\n  CATEGORY: {i.get("category")}\n  CONCEPT:{i.get("concept")}')
                                        break
                                    case "2":
                                        for position, i in enumerate(finance.sort_transactions(trans_list, "date"), start = 1):
                                            print(f'{position}) ID: {i.get("id")} {i.get("date")}\n  AMOUNT: {i.get("amount")}$\n  CATEGORY: {i.get("category")}\n  CONCEPT:{i.get("concept")}')
                                        break
                                
                                    case _:
                                        print("Error, Enter 1 for amount or 2 for date")
                            print("  -------------------------")

                        case "6":
                            break
                        case _:
                            print("Error, please enter a number between 1 and 6")

            case "4":
                while True:
                   sub_selection = input("Simulators SubMenu:\n 1) Compound Interest Calculator\n 2) Market Simulator\n 3) Calendar Planificator\n 4) Close SubMenu\n")
                   print("  -------------------------")
                   match sub_selection:
                        case "1":
                            print("Compund Interest Calculator:")
                            try:
                               initial_money = float(input("What is your initial aportation: "))
                               interest_rate = float((input("What would the interest rate be: ")))
                               years = int(float(input("How many years: ")))
                               final_money = utils.calculate_compound_interest(initial_money, interest_rate, years)
                               print(f"If you invest {initial_money} $ on a {interest_rate} % interest rate fund, in {years}, you would have {final_money}")
                               print("  -------------------------")
                            except AssertionError:
                                print("Error, The initial amount, years and interest rate must be higher than 0")
                                print("  -------------------------")
                            except ValueError:
                                print("Error, you must enter a number")
                                print("  -------------------------")

                        case "2":
                            print("Market Simulator:")
                            new = next(utils.market_sim())
                            print(f'Recomended Stock: {new["recomended_stock"]}, Variation: {new["variation"]}')
                            print("  -------------------------")
                        case "3":
                            print("Calendar Planificator:")
                            utils.calendar_planification()
                            print("  -------------------------")
                        case "4":
                            break
                        case _:
                            print("Error, that option is not avaiable, please enter a number beetwen 1 and 4")

            case "5":
                print("Expenses Categories Analysis:")
                trans_list = storage.load_transactions()
                historical_categories = ["Food", "Travel", "Job", "Subscriptions", "Shopping", "Utilities", "Investments"]
                finance.analyze_expenses_deviation(trans_list, historical_categories)
            
            case "6":
                print("Executed Functions History:")
                storage.load_app_log(app_log_path)

            case "7":
                print(f"Goodbye, {user_name} 👋")
                exit()

            case _:
                print("Error, that option is not avaiable, please enter a number beetwen 1 and 7")
