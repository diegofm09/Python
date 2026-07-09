from pathlib import Path
import json

main_path = Path(__file__).resolve().parent.parent

data_path = main_path/"data"
transactions_path = data_path/"transactions.json"
app_log_path = data_path/"app_log.txt"
config_path = main_path/"config.json"
clean_report_path = data_path/"clean_report.txt"

if not data_path.is_dir():
    data_path.mkdir()

if not transactions_path.exists():
    with open(transactions_path, "w") as file:
        transactions_list = []
        json.dump(transactions_list, file, indent = 2)

if not app_log_path.exists():
    app_log_path.touch()

try:
    with open(config_path, "x") as file:
        initial_data = {"user_name": "name", "currency": "EUR", "expense_limit": 500.00}
        json.dump(initial_data, file, indent=2)
except Exception:
    pass

def load_transactions():
    global transactions_list
    try:
        with open(transactions_path, "r") as file1:
            transactions_list = json.load(file1)
    except Exception:
        print("Error ocurred while loading transactions")
    finally:
        print("File Closed Safely")

def save_transactions():
    global transactions_list
    try:
        with open(transactions_path, "w") as file2:
            json.dump(transactions_list, file2, indent=2)
    except Exception:
        print("Error ocurred while saving transactions")
    finally:
        print("File Closed Safely")

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

def create_clean_reports(reports_list, file_path):
    with open(file_path, "w") as file3:
        for line in reports_list:
            file3.write(repr(line)+ "\n")

def load_app_log(file_path):
    with open(file_path, "r") as file4:
        while (line:=file4.readline()) != "":
            print(line)

