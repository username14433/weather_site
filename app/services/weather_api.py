import requests
from .. import models
from . import services
from .. import services

KEY = '7a14803889663b797929d5816688bd85'
api_city = 'Moscow'
api_country = 'Russia'


def get_coordinates_by_location_name(request, city, country, location=''):
    coordinates = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit={1}&appid={KEY}').json()
    lat = coordinates[0]['lat']
    lon = coordinates[0]['lon']
    print(coordinates)
    return lat, lon





def get_weather_data(request):
    lat, lon = get_coordinates_by_location_name(request)
    weather_data = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={KEY}').json()
    return weather_data



def get_weather_conditions(request):
    weather_data = get_weather_data(request)
    cloudiness = weather_data['weather'][0]['description']
    speed_wind = weather_data['wind']['speed']
    temperature = weather_data['main']['temp'] - 273.15
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    temp_feels_like = weather_data['main']['feels_like'] - 273.15
    visibility = weather_data['visibility']
    return {'cloudiness': cloudiness, 'speed_wind': speed_wind,
            'temperature': temperature, 'pressure': pressure,
            'humidity': humidity, 'temp_feels_like': temp_feels_like,
            'visibility': visibility}
