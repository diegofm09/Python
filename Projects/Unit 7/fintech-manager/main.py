from core import auth, finance, storage, utils
from pathlib import Path
import json, datetime

main_path = Path(__file__).resolve().parent

config_path = main_path/"config.json"

if __name__ == "__main__":
    storage.initialize_files()
    user_name = storage.change_name()
    while True:
        print("  -------------------------")
        selection = input("Menu Selection:\n 1) Profile and balance\n 2) Register Transaction\n 3) Advanced History\n 4) Investings and Simulator\n 5) Monthly Expenses Analysis\n 6) System Auditory\n 7) Close System\n")
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
                category = input("Enter the category: ")
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
                pass

            case "4":
                pass

            case "5":
                pass

            case "6":
                pass

            case "7":
                print(f"Goodbye, {user_name} 👋")
                exit()
                
            case _:
                print("Error, that option is not avaiable, please enter a number beetwen 1 and 7")
