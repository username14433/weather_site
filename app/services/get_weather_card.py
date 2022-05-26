from ..models import WeatherCard
def get_weather_card(kwargs):
    weather_card_slug = kwargs.get('slug')
    weather_card = WeatherCard.objects.get(slug=weather_card_slug)
    return {'weather_card_slug': weather_card_slug, 'weather_card': weather_card}

