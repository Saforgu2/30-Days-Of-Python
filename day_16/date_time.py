# DAY 16
# LEVEl 1

from datetime import time, date, datetime, timedelta

now = datetime.now()
print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.timestamp())

t = now.strftime("%m/%d/%Y, %H:%M:%S")
print(t)

string_time = "5 december, 2019"
object_time = now.strptime(string_time, "%d %B, %Y")
print(object_time)

new_year = datetime(year=2027, month=1, day=1)
time_left = new_year - now
print("Time left: ", time_left)

time_start = datetime(year=1970, month=1, day=1)
time_passed = now - time_start
print(time_passed)
