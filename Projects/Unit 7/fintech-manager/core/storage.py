from pathlib import Path
import json

main_path = Path(__file__).resolve().parent.parent

data_path = main_path/"data"
transactions_path = data_path/"transactions.json"
app_log_path = data_path/"app_log.txt"
config_path = main_path/"config.json"

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

def load_transactions(file):
    global transactions_list
    try:
        with open(file, "r") as file1:
            transactions_list = json.load(file1)
    except Exception:
        print("Error ocurred loading transactions list")