import datetime
import time
import json
from pathlib import Path

main_path =  Path(__file__).resolve().parent.parent
data_path = main_path/"data"
app_log_path = data_path/"app_log.txt"
config_path = main_path/"config.json"

def performance(function):
    def wrapper(*args, **kwargs):
        initial_time = time.time()
        result = function(*args, **kwargs)
        execution_time = time.time() - initial_time
        date_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(app_log_path, "a") as file:
            file.write(f"[{date_time}] - FUNCTION: {function.__name__} - EXECUTION TIME: {round(execution_time*1000, 3)}ms\n")
        return result
    return wrapper

def limit_verif():
    with open(config_path, "r") as file:
        config_dict = json.load(file)
        limit = config_dict.get("expense_limit")
    def evaluate(movement):
        if movement < 0:
            return abs(movement)<limit
        else:
            return True
    return evaluate

def dinamic_alerts(*args, **kwargs):
        if kwargs and "urgent" in kwargs and kwargs.get("urgent") == True:
            print("*****************")
        for arg in args:
            print(arg)
        if kwargs and "urgent" in kwargs and kwargs.get("urgent") == True:
            print("*****************")




