from pathlib import Path
import json
from .auth import performance
import datetime

main_path = Path(__file__).resolve().parent.parent

data_path = main_path/"data"
transactions_path = data_path/"transactions.json"
app_log_path = data_path/"app_log.txt"
config_path = main_path/"config.json"
clean_report_path = data_path/"clean_report.txt"

def initialize_files():
    if not data_path.is_dir():
        data_path.mkdir()


    if not transactions_path.exists():
        with open(transactions_path, "w") as file:
            transactions_list = [{
                    "id": 0,
                    "amount": 0,
                    "category": "Configuration",
                    "concept": "Initialization Transaction",
                    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                },]
            json.dump(transactions_list, file, indent = 2)


    if not app_log_path.exists():
        app_log_path.touch()


    try:
        with open(config_path, "x") as file:
            initial_data = {"user_name": "name", "currency": "EUR", "expense_limit": 500.00}
            json.dump(initial_data, file, indent=2)
    except Exception:
        pass

def change_name():
    with open(config_path, "r") as file:
        config_dict = json.load(file)
    if config_dict.get("user_name") == "name":
        config_dict["user_name"] = input("👋 Welcome, introduce your user name: ")
        with open(config_path, "w") as file:
            json.dump(config_dict, file, indent = 2)
            file.flush()
        return config_dict["user_name"]    
    else:
        while True:
            selection = input(f'Your current user name is {config_dict.get("user_name")}:\n -Enter 1 if you would lime to change it\n -Enter 2 if you want to leave it like that:\n')
            match selection:
                case "2":
                    print(f'Okey, Welcome {config_dict.get("user_name")} 👋')
                    break
                case "1":
                    config_dict["user_name"] = input("Okey, enter your new name: ")
                    break
                case _:
                    print("Error, please enter either 1 or 2")
        with open(config_path, "w") as file:
            json.dump(config_dict, file, indent = 2)
            file.flush()
        return config_dict["user_name"]

@performance
def load_transactions():
    try:
        with open(transactions_path, "r") as file1:
            return json.load(file1)
    except Exception:
        print("Error ocurred while loading transactions")
        return []
    finally:
        print("File Closed Safely")

@performance
def save_transactions(transactions_list):
    try:
        with open(transactions_path, "w") as file2:
            json.dump(transactions_list, file2, indent=2)
    except Exception:
        print("Error ocurred while saving transactions")
    finally:
        print("File Closed Safely")

@performance
def change_expense_limit(new_limit):
    with open(config_path, "r+") as file:
        new_limit_dict = json.load(file)
        current_pointer = file.tell()
        print(f"Current pointer position: {current_pointer}")
        new_limit_dict["expense_limit"] = new_limit
        
        file.seek(0)
        file.truncate()
        json.dump(new_limit_dict, file, indent=2)
        file.flush()

@performance
def create_clean_reports(reports_list, file_path):
    with open(file_path, "w") as file3:
        for line in reports_list:
            file3.write(repr(line)+ "\n")

@performance
def load_app_log(file_path):
    with open(file_path, "r") as file4:
        while (line:=file4.readline()) != "":
            print(line)
