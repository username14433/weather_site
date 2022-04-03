from django.db.models import Q
from django.views import View
from django.shortcuts import render, redirect
from .models import Location, WeatherCard
from . import forms
from .services import weather_card_creation, create_weather_card_for_home_page


class HomeView(View):
    def get(self, request):
        weather_card = create_weather_card_for_home_page.create_home_weather_card(request)
        form = forms.SearchForm()
        context = {'card': weather_card, 'form': form}
        return render(request, 'app/main.html',  context)


class SearchResultsView(View):
    def get(self, request):
        weather_card = create_weather_card_for_home_page.create_home_weather_card(request)
        context = {'card': weather_card}
        return render(request, 'app/search_results.html', context)
    def post(self, request):
        form = forms.SearchForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            city = form.cleaned_data['search_input']
            print(city)
            weather_card = weather_card_creation.create_weather_card_locaion(city)
            context['card'] = weather_card
            return redirect('search')
        return render(request, 'app/search_results.html', context)


class CityWeatherView(View):
    def get(self, request):
        query = self.request.GET.get('q')
        city_weather_conditions = WeatherCard.objects.filter(Q(city__icontains=query))
        context = {'city_weather_conditions': city_weather_conditions}
        return render(request, 'app/city_weather.html', context)



