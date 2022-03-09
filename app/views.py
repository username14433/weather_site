from django.db.models import Q
from django.views import View
from django.shortcuts import render
from django.views.generic import ListView
from .forms import SearchForm
from .models import Location, WeatherCard
from .services import weather_card_creation, operations_with_input_search, weather_api, services


class HomeView(View):
    def get(self, request):
        weather_conditions = weather_card_creation.create_weather_card(WeatherCard, request)
        context = {'weather_conditions': weather_conditions}
        return render(request, 'app/main.html', context)


class SearchResultsView(ListView):
    def post(self, request):
        pass
        # query = operations_with_input_search.get_search_input(request)
        # self.location = Location.objects.create(city=query['city'], country=query['country'])
        # model = Location
        # template_name = 'app/search_results.html'
        # self.card = WeatherCard.objects.filter(location=self.location)
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Location.objects.filter(Q(city__icontains=query) | Q(country__icontains=query))
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['card'] = WeatherCard.objects.filter(location=self.location)
        return context


class CityWeatherView(View):
    def get(self, request):
        query = self.request.GET.get('q')
        city_weather_conditions = WeatherCard.objects.filter(Q(city__icontains=query) | Q(country__icontains=query))
        context = {'city_weather_conditions': city_weather_conditions}
        return render(request, 'app/city_weather.html', context)
