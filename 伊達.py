from datetime import date
t=date(2020,12,24)
print(t)
print(t.weekday())
# 0 Monday~6 Sunday

from datetime import datetime
n=datetime.now()
print(n)

from datetime import datetime, timedelta
d1=datetime(2020,12,25,0,0,0)
d2=datetime(2020,11,25,0,0,0)
result=d1-d2
print(result)
print(result.days)

from datetime import datetime, timedelta,timezone
JST=timezone(timedelta(hours=+9))
result=datetime(2020,1,1,12,15,30,tzinfo=JST)
print(result)

import jpholiday 
from datetime import datetime

d=datetime(2021,5,3)
result=jpholiday.is_holiday_name(d)
print(result)

import jpholiday
result= jpholiday.year_holidays(2025)
print(result)


