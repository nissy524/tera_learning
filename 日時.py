from dateutil.relativedelta import relativedelta
from datetime import datetime

today=datetime.today()
print(today)

d1=today+relativedelta(months=7)
print(d1)

from datetime import datetime
today=datetime.today()
print(today)
today_str=today.strftime('%Y年%m月%d日')
print(today_str)

import calendar
c=calendar.month(2002,5)
print(c)

import calendar
w,days=calendar.monthrange(2020,2)
print(days)
