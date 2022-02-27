from django.contrib import admin

from .models import WeatherCard, City

models = (WeatherCard, City)
for model in models:
    admin.site.register(model)
