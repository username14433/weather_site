import requests

KEY = '7a14803889663b797929d5816688bd85'
api_city = 'Moscow'
api_country = 'Russia'
KELVINS = 273.15

def get_coordinates_by_location_name(city,):
    coordinates = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={1}&appid={KEY}').json()
    lat = coordinates[0]['lat']
    lon = coordinates[0]['lon']
    return lat, lon




def get_weather_data(city):
    lat, lon = get_coordinates_by_location_name(city)
    weather_data = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={KEY}').json()
    return weather_data



def get_weather_conditions(city):
    weather_data = get_weather_data(city)
    cloudiness = weather_data['weather'][0]['description']
    speed_wind = weather_data['wind']['speed']
    temperature = weather_data['main']['temp'] - KELVINS
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    temp_feels_like = weather_data['main']['feels_like'] - KELVINS
    visibility = weather_data['visibility']
    return {'cloudiness': cloudiness, 'speed_wind': speed_wind,
            'temperature': round(temperature), 'pressure': pressure,
            'humidity': humidity, 'temp_feels_like': round(temp_feels_like),
            'visibility': visibility}
