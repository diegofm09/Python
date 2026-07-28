import datetime
import random

def calculate_compound_interest(initial_money, interest_rate, years):
    assert initial_money>0 and interest_rate>=0 and years>0
    for i in range(years):
        initial_money += (initial_money*interest_rate)/100
    return round(initial_money, 3)

def calendar_planification():
    actual_time = datetime.datetime.now()
    one_month = datetime.timedelta(days=30)
    plus_one_month = (actual_time + one_month).strftime("%d/%m/%Y %H:%M:%S")
    plus_two_month = (actual_time + one_month*2).strftime("%d/%m/%Y %H:%M:%S")
    plus_three_month = (actual_time + one_month*3).strftime("%d/%m/%Y %H:%M:%S")
    print(f'Today is {actual_time.strftime("%d/%m/%Y %H:%M:%S")}:\n -In 30 days it will be {plus_one_month}\n -In 60 days it will be {plus_two_month}\n -In 90 days it will be {plus_three_month}')

def market_sim(seed_numb=None):
    if seed_numb:
        random.seed(seed_numb)
    stocks = ["AAPL", "NVDA", "GOOG", "MSFT", "AMZN", "AVGO", "META", "SPCX", "TSLA"]
    while True:
        variation = round(random.uniform(-4.5, 4.5), 2)
        yield {"recomended_stock": random.choice(stocks), "variation": variation}