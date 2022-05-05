from django.views import View
from django.shortcuts import render, redirect
from .models import Location, WeatherCard, ChosenWeatherCard
from . import forms
from .services import weather_card_creation, create_weather_card_for_home_page, get_weather_card, config

class HomeView(View):
    def get(self, request):
        user = request.user
        user.auntificate()
        city = config.BASE_CITY
        weather_card = weather_card_creation.create_weather_card_locaion(request, city)
        form = forms.SearchForm()
        context = {'card': weather_card, 'form': form}
        return render(request, 'app/main.html',  context)


class SearchResultsView(View):
    def get(self, request):
        form = forms.SearchForm(request.POST or None)
        city = form.cleaned_data['city']
        weather_card = weather_card_creation.create_weather_card_locaion(request, city)
        weather_cards = WeatherCard.objects.filter(user=request.user)
        context = {'card': weather_card, 'form': form}
        return render(request, 'app/search_results.html', context)
    def post(self, request):
        form = forms.SearchForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_card = weather_card_creation.create_weather_card_locaion(request, city)
            context['card'] = weather_card
            context['city'] = city
        return render(request, 'app/search_results.html', context)


class CityWeatherView(View):
    def get(self, request):
        return render(request, 'app/city_weather.html', {})


class ChosenCityWeather(View):
        def get(self, request, **kwargs):
            user = request.user
            card = get_weather_card.get_weather_card(kwargs)
            #получить карточку на котрую нажали по id или по request (посмотреть документацию)
            card.bookmark = True
            cards = WeatherCard.objects.filter(bookmard=True)
            context = {'cards': cards}
            return render(request, 'app/chosen_weather_cities.html', context)

# class BookmarkWeatherCard(View):
#     def get(self, request, **kwargs):
#         user = request.user
#         card = get_weather_card.get_weather_card(kwargs)
#         #получить карточку на котрую нажали по id или по request (посмотреть документацию)
#         card.bookmark = True
#         cards = WeatherCard.objects.filter(bookmard=True)
#         context = {'cards': cards}
#         return render(request, 'app/chosen_weather_cities.html', context)



