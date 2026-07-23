import random

def data_extractor(movement_list, category = None):
        for movement in movement_list:
            if not category or movement.get("category") == category:
                yield movement 

def add_international_movements(function_data_extractor_variable):
    international_movements = [
    {
        "amount": -45.00,
        "category": "Subscriptions",
        "concept": "US Cloud Server (AWS)"
    },
    {
        "amount": 120.50,
        "category": "Investments",
        "concept": "S&P 500 Dividend"
    },
    {
        "amount": -89.99,
        "category": "Shopping",
        "concept": "Amazon US Tech Purchase"
    },
    {
        "amount": -15.00,
        "category": "Entertainment",
        "concept": "Spotify Premium US"
    },
    {
        "amount": -210.00,
        "category": "Travel",
        "concept": "Hotel Booking Tokyo"
    },
    {
        "amount": 350.00,
        "category": "Freelance",
        "concept": "International Client Wire Transfer"
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