import datetime as dt

# 2
# now = dt.datetime.now()
# time = now.strftime ("%m/%d/%Y, %H:%M:%S")
# print (time)

# 3
# date_string = "5 December, 2019"
# converted = dt.datetime.strptime (date_string,"%d %B, %Y")

# print (converted)

new_year = dt.date(day=1, month=1, year=2027)
today = dt.date.today()
difference = (new_year - today)
print(difference)
