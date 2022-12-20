#https://docs.python.org/3/library/zoneinfo.html

#ZoneInfo a partir de versión 3.9 de Python

from zoneinfo import ZoneInfo, available_timezones
from datetime import datetime

print(available_timezones())#En windows --> Conjunto vacío --> pip install tzdata

zi_los_angeles = ZoneInfo(key="America/Los_Angeles")
zi_madrid = ZoneInfo(key="Europe/Madrid")

dt = datetime(year=2022, month=12, day=19, hour=2, minute=3, tzinfo=ZoneInfo(key="America/Los_Angeles"))
print(dt)
print(dt.astimezone(zi_madrid))