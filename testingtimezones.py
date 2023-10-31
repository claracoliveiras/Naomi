from datetime import datetime, date
import pytz

zones = pytz.all_timezones
print(datetime.now().date())

firstDate = date(2023, 9, 1)
secondDate = date(2023, 12, 1)

dates = (date(2023, 10, 11), date(2023, 10, 11), date(2023, 12, 11), date(2023, 10, 12), date(2023, 10, 31), date(2023, 12, 2))
search = []

for date in dates:
    if firstDate < date and secondDate > date:
        search.append(date)

print(search)