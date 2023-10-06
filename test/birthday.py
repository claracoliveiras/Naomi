import parsedatetime
from datetime import datetime

cal = parsedatetime.Calendar()
print(cal.parse("july 7th 2004"))

time_struct, parse_status = cal.parse("tomorrow")
dt = datetime(*time_struct[:6])

print(int(dt.timestamp()))

