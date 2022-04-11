from weather import get_location
from pyowm import *

APIKEY = 'edcacfd8339871d9f0f7f6e48e1b08eb'
OpenWMap = OWM(APIKEY)
mrg = OpenWMap.weather_manager()
mrg_code = OpenWMap.geocoding_manager()

def lat():
    L_location = mrg_code.geocode(get_location())
    location = L_location[0]
    return location.lat

def lon():
    L_location = mrg_code.geocode(get_location())
    location = L_location[0]
    return location.lon


def forecast_temp():
    one_call = mrg.one_call(lat=lat(), lon=lon())
    temp = []
    for i in range(0, 6):
        temp.append(one_call.forecast_hourly[i].temperature('fahrenheit').get('temp'))
    print("f temp: " +str(temp))
    return temp


