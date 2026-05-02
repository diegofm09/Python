import datetime
now = datetime.datetime.now()
formated = now.strftime("Today is %A%e of %B of %Y")
print(formated)

time_string = "09:23:17 18-02-1964"
formated_string = datetime.datetime.strptime(time_string, "%H:%M:%S %d-%m-%Y")
print(formated_string)