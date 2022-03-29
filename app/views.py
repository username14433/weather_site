from django.db.models import Q
from django.views import View
from django.shortcuts import render, redirect
from .models import Location, WeatherCard
from .services import weather_card_creation, create_weather_card_for_home_page


class HomeView(View):
    def get(self, request):
        weather_card = create_weather_card_for_home_page.create_home_weather_card(request)
        context = {'card': weather_card}
        return render(request, 'app/main.html',  context)


class SearchResultsView(View):
    def get(self, request):
        weather_card = weather_card_creation.create_weather_card_locaion(request)
        context = {'card': weather_card}
        return render(request, 'app/search_results.html', context)
    def post(self, request):
        city = request.POST.get('q')
        weather_card = weather_card_creation.create_weather_card_locaion(request)
        context = {'card': weather_card, 'city': city}
        return render(request, 'app/search_results.html', context)


class CityWeatherView(View):
    def get(self, request):
        query = self.request.GET.get('q')
        city_weather_conditions = WeatherCard.objects.filter(Q(city__icontains=query))
        context = {'city_weather_conditions': city_weather_conditions}
        return render(request, 'app/city_weather.html', context)



