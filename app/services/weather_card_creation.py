from . import weather_api
from .. import services
from . import operations_with_input_search, create_elements_for_weather_card, get_weather_card, config
from .. models import Location, WeatherCard
def create_weather_card_locaion(kwargs, city):
    rain_chance = create_elements_for_weather_card.create_daypart_rain_chance()['rain_chance']
    part_of_the_day = create_elements_for_weather_card.create_daypart_rain_chance()['part_of_the_day']
    if not city:
        city = config.BASE_CITY
    weather_data = services.weather_api.get_weather_conditions(city)
    slug = get_weather_card.get_weather_card(kwargs)['weather_card_slug']
    location = Location.objects.create(city=city)
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
                                              slug=slug
                                              )
    return weather_card
