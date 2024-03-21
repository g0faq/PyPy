import datetime as dt


date = (dt.date.today() + dt.timedelta(days=int(input())))
print(date.day, date.month)
