from django.urls import path
from .views import HomeView, SearchResultsView, CityWeatherView, ChosenCityWeather

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('city_weather/', CityWeatherView.as_view(), name='city_weather'),
    path('chosen weather cities/', ChosenCityWeather.as_view(), name='bookmark_weather')
]