import datetime

target1 = datetime.datetime(2027, 4, 12, 19, 24, 12)
target2 = datetime.datetime(2025, 11, 9, 4, 57, 20)
actual = datetime.datetime.now()
print(f"{target1} is in the future") if target1>actual else print(f"{target1} is the past")
print(f"{target2} is in the future") if target2>actual else print(f"{target2} is the past")