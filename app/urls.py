from django.urls import path
from .views import HomeView, SearchResultsView, CityWeatherView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('city_weather/', CityWeatherView.as_view(), name='city_weather'),

]