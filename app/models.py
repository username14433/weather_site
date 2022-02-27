from django.db import models


class City(models.Model):
    name = models.CharField(verbose_name="Название города", max_length=255)
    country = models.CharField(verbose_name="Страна", max_length=255)


class WeatherCard(models.Model):
    temperature = models.IntegerField(verbose_name="Температура")
    humidity = models.IntegerField(verbose_name='Влажность')
    pressure = models.IntegerField(verbose_name="Давление")
    rain_chance = models.IntegerField(verbose_name="Вероятность дождя")
    part_of_the_day = models.CharField(verbose_name="Часть дня", max_length=15)
    name = models.CharField(verbose_name='Город', max_length=65)
    country = models.CharField(verbose_name='Страна', max_length=65)
    def __str__(self):
        return str(self.id)





