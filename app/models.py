from django.db import models


class Location(models.Model):
    city = models.CharField(verbose_name="Название города", max_length=255)
    country = models.CharField(verbose_name="Страна", max_length=255)


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
