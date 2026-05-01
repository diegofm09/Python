import datetime
today = datetime.date.today()
print(today)
week = datetime.timedelta(weeks = 2)
print(f"Today is {today}, in 2 weeks its going to be {today+week}")
bdate = datetime.date(2027,4,29)
print(f"Till my birthday there are {bdate-today} days")