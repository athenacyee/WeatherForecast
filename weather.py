from pyowm import *
from datetime import datetime


APIKEY = 'API'
OpenWMap = OWM(APIKEY)
mrg = OpenWMap.weather_manager()
observation = ""
weather = ""



def get_curenttime():
    now = datetime.now()
    current_time = now.strftime('%Y-%m-%d %H:%M')
    return current_time


def input_location(location):
    global observation, weather
    observation = mrg.weather_at_place(location)
    weather = observation.weather
    print(observation.location.name)

def get_location():
    return observation.location.name


def get_sunset():
    sunset_unix = weather.sunset_time()  # default unit: 'unix'
    sunset_time = datetime.fromtimestamp(
        int(sunset_unix)
    ).strftime('%H:%M')
    print(sunset_time)
    return sunset_time


def get_sunrise():
    sunrise_unix = weather.sunrise_time()
    sunrise_time = datetime.fromtimestamp(
        int(sunrise_unix)
    ).strftime('%H:%M')
    print(sunrise_time)
    return sunrise_time


def get_temp():
    temperature = weather.temperature('fahrenheit')
    print(temperature)
    temp = str(temperature['temp'])
    return temp


def get_status():
    status = weather.detailed_status
    print(status)
    return status


def get_windspeed():
    wind = weather.wind(unit='miles_hour')
    print(wind)
    windspeed = str("{:.2f}".format(wind['speed']))
    return windspeed


