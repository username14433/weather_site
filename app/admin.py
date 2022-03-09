from django.contrib import admin
from . import models

models = (models.Location, models.WeatherCard)

admin.site.register(models)
