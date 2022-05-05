from . import weather_api
from .. import services
from . import create_elements_for_weather_card
from .. models import Location, WeatherCard
def create_home_weather_card(request):
    rain_chance = create_elements_for_weather_card.create_daypart_rain_chance()['rain_chance']
    part_of_the_day = create_elements_for_weather_card.create_daypart_rain_chance()['part_of_the_day']
    weather_data = services.weather_api.get_weather_conditions('Moscow')
    location = Location.objects.create(city='Moscow')
    print('------', weather_data['temperature'])
    weather_card = WeatherCard.objects.create(temperature=weather_data['temperature'],
                                              pressure=weather_data['pressure'],
                                              rain_chance=rain_chance,
                                              humidity=weather_data['humidity'],
                                              visibility=weather_data['visibility'],
                                              cloudiness=weather_data['cloudiness'],
                                              temp_feels_like=weather_data['temp_feels_like'],
                                              speed_wind=weather_data['speed_wind'],
                                              part_of_the_day=part_of_the_day,
                                              location=location,
                                              user=request.user
                                              )
    return weather_card