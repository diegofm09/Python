import random

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
    analysis = {"net_balance": 0, "highest_income": 0, "highest_spend": 0}
    trans_list_amounts = [i.get("amount") for i in trans_list]
    analysis["net_balance"] = round(sum(trans_list_amounts), 3)
    analysis["highest_spend"] = min(trans_list_amounts)
    analysis["highest_income"] = max(trans_list_amounts)
    return analysis

def filter_transactions(trans_list, minimum_value):
    pass