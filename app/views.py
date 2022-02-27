from django.db.models import Q
from django.views import View
from django.shortcuts import render
from django.views.generic import ListView
from .forms import SearchForm

from .models import WeatherCard, City
class HomeView(View):
    def get(self, request):
        weather_conditions = WeatherCard.objects.all()
        context = {'weather_conditions': weather_conditions}
        return render(request, 'app/main.html', context)

class SearchResultsView(ListView):
    model = City
    template_name = 'app/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        objects_list = City.objects.filter(Q(name__icontains=query) | Q(country__icontains=query))
        return objects_list

class CityWeatherView(View):
    def get(self, request):
        query = self.request.GET.get('q')
        city_weather_conditions = WeatherCard.objects.filter(Q(name__icontains=query) | Q(country__icontains=query))
        context = {'city_weather_conditions': city_weather_conditions}
        return render(request, '')


