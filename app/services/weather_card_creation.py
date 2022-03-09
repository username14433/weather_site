from .. import models
from . import weather_api
from .. import services

def create_weather_card(model, request):
    weather_data = services.weather_api.get_weather_conditions(request)
    weather_card = model.objects.create(temperature=weather_data['temperature'],
                         pressure=weather_data['pressure'],
                         humidity=weather_data['humidity'],
                         visibility=weather_data['temp_feels_like'],
                         cloudiness=weather_data['visibility'],
                         temp_feels_like=weather_data['cloudiness'],
                         speed_wind=weather_data['speed_wind'])

