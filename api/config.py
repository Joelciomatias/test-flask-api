import os

# WEATHER_API_KEY = os.environ['WEATHER_API_KEY']
# WEATHER_API_URL = os.environ['WEATHER_API_URL']

CACHE_TIMEOUT = os.environ.get('CACHE_TIMEOUT')
LAST_SEARCHED_CITIES = os.environ.get('LAST_SEARCHED_CITIES')

CACHE_TIMEOUT = int(CACHE_TIMEOUT) if CACHE_TIMEOUT else 300
last_searched_cities = int(LAST_SEARCHED_CITIES) if LAST_SEARCHED_CITIES else 5



WEATHER_API_KEY='155a4457745da019871ac8d5348a9639'
WEATHER_API_URL='https://api.openweathermap.org/data/2.5/weather'