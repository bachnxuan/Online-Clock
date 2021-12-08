# import turtle 

# t = turtle.Turtle()

# #t.circle(120)
# t.pencolor('orange')
# t.pensize(10)
# t.right(144)
# t.forward(120)
# t.right(144)
# t.forward(120)
# t.right(144)
# t.forward(120)
# t.right(144)
# t.forward(120)
# t.right(144)
# t.forward(120)

# turtle.mainloop()

# from datetime import datetime
# from time import sleep as wait
# import os
# while True:
#     now = datetime.now()

#     full_clock = now.strftime("%H:%M:%S")
#     day = now.strftime("%Z %z")
#     print(f"{day}")
#     print(now)
#     wait(1)

#     os.system('cls')

                                   

import urllib.request
import json
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import datetime as dt
from time import sleep as wait
import pytz

with urllib.request.urlopen("https://geolocation-db.com/json") as url:
    data = json.loads(url.read().decode())

geolocator = Nominatim(user_agent="geoapiExercises")
lad = data['country_name']
location = geolocator.geocode(lad)
obj = TimezoneFinder()
tzr = obj.timezone_at(lng=location.longitude, lat=location.latitude)

source_date = dt.datetime.now()

currentTimeZone = pytz.timezone(tzr)
currentDateWithTimeZone = currentTimeZone.localize(source_date)
import os
connect = os.system('ping google.com')
while True:
    if connect == 1:
        break
    print("-----WELCOME TO CLIENT ONLINE CLOCK-----")
    print(f"Country : {lad}")
    print(f'Time Zone Is Set To : {tzr}')
    now = dt.datetime.now(tz=currentTimeZone)

    full_clock = now.strftime("%I:%M:%S %p")
    day = now.strftime("%A %d-%m-%Y")
    print(f"{day}")
    print(f"{full_clock}")
    wait(0.1)
    os.system('cls')