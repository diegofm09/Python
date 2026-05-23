import time
import datetime

counter = 0

def show_time(funct):
    def wrapper(*args, **kwargs):
        initial_time = time.time()
        result = funct(*args, **kwargs)
        final_time = time.time()
        print(f"Execution time: {round(final_time-initial_time, 5)}")
        return result
    global counter
    counter += 1
    return wrapper

def date_validator(user_date):
    try:
        assert "-" in user_date, "Error, you have to write the date with hyphen"
        final_date = datetime.datetime.strptime(user_date, "%d-%m-%Y").date()
        if final_date > datetime.date.today():
            raise ValueError("That date is from the future")
        return final_date
    except AssertionError as e:
        print(e)
    except ValueError as e:
        print("Error, the format of the date must be 'day-month-year'")
        print(e)
