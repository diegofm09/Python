import time
import random
import datetime

def download():
    print("Downloading...")
    time.sleep(random.randint(2,5))
    print("Downloaded")
download()


hour = datetime.datetime.now()
formated = datetime.datetime.strftime(hour, "%d-%b-%Y %H:%M")
print(formated)


important_dates = [datetime.date(2026,12,25), datetime.date(2026,12,31), datetime.date(2026,10,31), datetime.date(2026,11,1), datetime.date(2026,5,1)]
print(random.choice(important_dates))


time.sleep(3)


init_time = time.time()
for i in range(100000):
    print(i)
final_time = time.time()
diference = final_time - init_time
print(diference)