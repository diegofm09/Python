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
    analysis = {"net balance": None, "highest income": None, "highest spend": None}
    for i in trans_list:
        pass