from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Location(models.Model):
    city = models.CharField(verbose_name="Название города", max_length=255, default="Moscow")


class WeatherCard(models.Model):
    temperature = models.IntegerField(verbose_name="Температура")
    humidity = models.IntegerField(verbose_name='Влажность')
    pressure = models.IntegerField(verbose_name="Давление")
    rain_chance = models.IntegerField(verbose_name="Вероятность дождя")
    part_of_the_day = models.CharField(verbose_name="Часть дня", max_length=15)
    visibility = models.CharField(verbose_name='Видимость', max_length=25)
    speed_wind = models.CharField(verbose_name='Скорость ветра', max_length=25)
    cloudiness = models.CharField(verbose_name="Облачность", max_length=25)
    temp_feels_like = models.CharField(verbose_name="Ощущается как", max_length=25)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Локация')
    # user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)
    bookmark = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, verbose_name="Слаг", null=True)

    def get_absolute_url(self):
        return reverse('card', kwargs={'slug': self.slug})

    def __str__(self):
        return f"Погода в {self.location}"


class ChosenWeatherCard(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', null=True, blank=True,
                             on_delete=models.CASCADE)
    card = models.ForeignKey(WeatherCard, verbose_name="Погодная карточка", on_delete=models.CASCADE, null=True,
                             blank=True)

    def __str__(self):
        return f"Погода в {self.card.location}"
