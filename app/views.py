from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from .models import Location, WeatherCard, ChosenWeatherCard
from .forms import SearchForm, RegistrationForm
from .services import weather_card_creation, create_weather_card_for_home_page, get_weather_card, config

class HomeView(View):
    def get(self, request):
        city = config.BASE_CITY
        weather_card = weather_card_creation.create_weather_card_locaion(request, city)
        form = SearchForm()
        context = {'card': weather_card, 'form': form}
        return render(request, 'app/main.html',  context)


class SearchResultsView(View):
    def get(self, request):
        form = SearchForm(request.POST or None)
        city = form.cleaned_data['city']
        weather_card = weather_card_creation.create_weather_card_locaion(request, city)
        weather_cards = WeatherCard.objects.filter(user=request.user)
        context = {'card': weather_card, 'form': form}
        return render(request, 'app/search_results.html', context)
    def post(self, request):
        form = SearchForm(request.POST or None)
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

class Regitsration(View):
    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}

        return render(request, 'app/registration.html', context)
    def post(self, request):
        form = RegistrationForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            new_user = form.save(commit=False)
            new_user.save()
            new_user.username = form.cleaned_data['username']
            new_user.password = form.cleaned_data['password']
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return redirect(request, 'app/registration.html', context)

# class BookmarkWeatherCard(View):
#     def get(self, request, **kwargs):
#         user = request.user
#         card = get_weather_card.get_weather_card(kwargs)
#         #получить карточку на котрую нажали по id или по request (посмотреть документацию)
#         card.bookmark = True
#         cards = WeatherCard.objects.filter(bookmard=True)
#         context = {'cards': cards}
#         return render(request, 'app/chosen_weather_cities.html', context)



