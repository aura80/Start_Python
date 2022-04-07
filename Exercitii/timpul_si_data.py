import time
import datetime
from datetime import date, timedelta

next_day = datetime.datetime.today() + datetime.timedelta(days=1)
next_day20 = datetime.datetime.today() + datetime.timedelta(days=20)
next_day_detailed = next_day.strftime('%B %d, %Y')
next_day20_detailed = next_day20.strftime('%B %d, %Y')

print(next_day_detailed)
print(next_day20_detailed)

if next_day_detailed[-8] == "0":
    next_day_detailed = next_day_detailed.replace(next_day_detailed[-8], "", 1)
print("conversion of next day: ", next_day_detailed)

if next_day20_detailed[-8] == "0":
    next_day20_detailed = next_day20_detailed.replace(next_day20_detailed[-8], "", 1)
print("conversion of 20+ day: ", next_day20_detailed)




