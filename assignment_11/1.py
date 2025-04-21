import pandas as pd
import datetime as dt
#Date time object for Jan 15 2012.
date=pd.Timestamp(year=2012, month=1,day=15)
print(date.day, "-", date.month, "-", date.year)
print(date)
#Specific date and time of 9:20 pm.
date=pd.Timestamp(year=2004, month=12,day=22, hour=21, minute=20)
print(date.day, "-", date.month, "-", date.year,":", date.hour, "hours", date.minute, "minutes")
print(date)
#Local date and time.
local_date=pd.Timestamp.now(tz='Asia/Kolkata')
print(local_date)
#A date without time.
print(date.date())
#Current date.
print(pd.Timestamp.now(tz='Asia/Kolkata').date())
#Time from a date time.
dt_obj=dt.datetime.now()
pd_obj=pd.to_datetime(dt_obj)
print(pd_obj.time())
#Current local time.
print(local_date.time())