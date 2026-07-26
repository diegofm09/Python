import random
from pathlib import Path
import json

main_path = Path(__file__).resolve().parent.parent
config_path = main_path/"config.json"

def data_extractor(movement_list, category = None):
        for movement in movement_list:
            if not category or movement.get("category") == category:
                yield movement 

def add_international_movements(function_data_extractor_variable):
    international_movements = [
    {
        "id": 901,
        "amount": -45.00,
        "category": "Subscriptions",
        "concept": "US Cloud Server (AWS)",
        "date": "2026-07-21 10:39:02",
    },
    {
        "id": 902,
        "amount": 120.50,
        "category": "Investments",
        "concept": "S&P 500 Dividend",
        "date": "2026-07-19 18:20:54",
    },
    {
        "id": 903,
        "amount": -89.99,
        "category": "Shopping",
        "concept": "Amazon US Tech Purchase",
        "date": "2026-07-20 03:02:12",
    },
    {
        "id": 904,
        "amount": -15.00,
        "category": "Entertainment",
        "concept": "Spotify Premium US",
        "date": "2026-07-21 19:52:53",
    },
    {
        "id": 905,
        "amount": -210.00,
        "category": "Travel",
        "concept": "Hotel Booking Tokyo",
        "date": "2026-07-21 13:29:52",
    },
    {
        "id": 906,
        "amount": 350.00,
        "category": "Freelance",
        "concept": "International Client Wire Transfer",
        "date": "2026-07-23 23:07:02"
    }
    ]
    for i in function_data_extractor_variable:
        yield i 
    international_movements_random = random.sample(international_movements, random.randint(2,3))
    for i in international_movements_random:
        yield i

def analyze_transactions(trans_list):
    analysis = {"net_balance": 0, "highest_income": 0, "highest_expense": 0}
    trans_list_amounts = [i.get("amount") for i in trans_list]
    analysis["net_balance"] = round(sum(trans_list_amounts), 3)
    analysis["highest_expense"] = min(trans_list_amounts)
    analysis["highest_income"] = max(trans_list_amounts)
    return analysis

def filter_transactions(trans_list, minimum_value):
    with open(config_path, "r") as file:
        configs = json.load(file)
    filtered_trans_list = list(filter(lambda x: x.get("amount")>=minimum_value, trans_list))
    string_trans_list = list(map(lambda x: f"{x.get('concept')}: {x.get('amount')} {configs['currency']}", filtered_trans_list))
    ids = [i.get("id") for i in filtered_trans_list]
    ziped_trans_list = list(zip(ids, string_trans_list))
    return ziped_trans_list

def get_expenses(trans_list):
    return [i.get("concept").upper() for i in trans_list if i.get("amount")<0]

def get_categorys(trans_list):
    return {i.get("category") for i in trans_list}

def easy_read(trans_list):
    return  {i.get("id"): (i.get("category"), i.get("amount")) for i in trans_list}

#mete aqui lo de ordenarlas por fecha
def sort_transactions(trans_list, sort_key):
    if sort_key == "money":
        sorted(trans_list, key = lambda x: x.get("amount"))
        return trans_list
    elif sort_key == "date":
        sorted(trans_list, )
    else:
        return trans_list
    
def categorys_analysis():
    pass
