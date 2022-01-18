import urllib.request
import json
from geopy.geocoders import Nominatim
from pyglet import event
from timezonefinder import TimezoneFinder
import datetime as dt
from time import sleep as wait
import pytz
import os
import keyboard
import pyglet
import platform

chk = platform.system()

try:
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
except:
    print("Please Reopen The App | We Have A Error !")
    print("The App Close In 2 Seconds...")
    wait(2)
    exit()

def cls():
    if chk != "Windows":
        os.system("clear")
    else:
        os.system("cls")


def option():
    cls()
    print("MENU\n\
    Exit [g]\n\
    Clock [s]\n\
    Countdown Clock [d]")
    while True:
        if keyboard.is_pressed("g"):
            exit()
        if keyboard.is_pressed("s"):
            olClock()
        if keyboard.is_pressed("d"):
            MainCCL()


def olClock():
    while True:
        if keyboard.is_pressed("f"):
            option()
        if keyboard.is_pressed("g"):
            exit()
        print("-----WELCOME TO ONLINE CLOCK-----")
        print(f"Country : {lad}")
        print(f'Time Zone Is Set To : {tzr}')
        now = dt.datetime.now(tz=currentTimeZone)

        full_clock = now.strftime("%I:%M:%S %p")
        day = now.strftime("%A %d-%m-%Y")
        print(f"{day}")
        print(f"{full_clock}")
        print("\n \nMenu [f]\nExit [g]")
        wait(0.4)
        cls()


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        wait(1)
        t -= 1

    print('Finish !')
    
    music = pyglet.resource.media('Nhac.mp3') 
    music.play()

    wait(1.5)

    option()
    
sec = 0

def MainCCL():
    secmain = 0
    while True:
        print("+1 sec [h]")
        print("-1 second [j]")
        print("Menu [f]")
        print("OK [Enter]")
        if keyboard.is_pressed("h"):
            secmain += 1
        if keyboard.is_pressed("j"):
            secmain -= 1
        if keyboard.is_pressed("f"):
            option()
        print(f"Second : {secmain}")
        sec = secmain
        if secmain < 0:
            print("We Have A Error")
            print("The App Return To Menu In 2 Seconds...")
            wait(2)
            option()
        if keyboard.is_pressed("enter"):
            break
        wait(0.3)
        cls()
    cls()
    countdown(int(sec))
