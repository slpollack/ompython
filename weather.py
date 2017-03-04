import forecastio
from geopy.geocoders import Nominatim
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather(location):
	api_key = os.environ['FORECASTIO_API_KEY']
	geolocator = Nominatim()
	latitude = geolocator.geocode(location).latitude
	longitude = geolocator.geocode(location).longitude
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
	return "{} and {}".format(forecast.summary, forecast.temperature)



# print(location.address)
#Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
# print((location.latitude, location.longitude))
#(40.7410861, -73.9896297241625)
# print(location.raw)
#{'place_id': '9167009604', 'type': 'attraction', ...}

