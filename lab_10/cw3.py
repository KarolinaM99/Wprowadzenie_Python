import time
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

czas = input("Podaj czas w formacie HH:MM:SS - ")
czas2 = datetime.strptime(czas, '%H:%M:%S')
print("Tokyo: ",datetime(2023, 5, 11, czas2.hour, czas2.minute, czas2.second, tzinfo=ZoneInfo("Asia/Tokyo")))
print("Waszyngton: ",datetime(2023, 5, 11, czas2.hour, czas2.minute, czas2.second, tzinfo=ZoneInfo("America/New_York")))
print("Sydney: ",datetime(2023, 5, 11, czas2.hour, czas2.minute, czas2.second, tzinfo=ZoneInfo("Australia/Sydney")))
print("Londyn: ",datetime(2023, 5, 11, czas2.hour, czas2.minute, czas2.second, tzinfo=ZoneInfo("Europe/London")))