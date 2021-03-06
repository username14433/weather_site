from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .models import Location, WeatherCard, ChosenWeatherCard
from .forms import SearchForm, RegistrationForm
from .services import weather_card_creation, create_weather_card_for_home_page, get_weather_card, config, create_elements_for_weather_card

class HomeView(View):
    def get(self, request):

        form = SearchForm()
        context = {'form': form}
        return render(request, 'app/main.html',  context)


class SearchResultsView(View):
    def get(self, request, **kwargs):
        form = SearchForm(request.POST or None)
        city = form.cleaned_data['city']
        weather_card = weather_card_creation.create_weather_card_locaion(kwargs, city)
        part_of_the_day = create_elements_for_weather_card.create_daypart_rain_chance()['part_of_the_day']
        weather_cards = WeatherCard.objects.filter(city=city)
        context = {'card': weather_cards, 'form': form, 'part_of_the_day': part_of_the_day,
                   'day': config.DAY, 'morning': config.MORNING, 'evening': config.EVENING}
        return render(request, 'app/search_results.html', context)
    def post(self, request, **kwargs):
        form = SearchForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_card = weather_card_creation.create_weather_card_locaion(kwargs, city)
            context['card'] = weather_card
            context['city'] = city
        return render(request, 'app/search_results.html', context)

class WeatherCardView(DetailView):
    model = WeatherCard
    context_object_name = 'card'
    template_name = 'app/city_weather.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CityWeatherView(View):
    def get(self, request):
        return render(request, 'app/city_weather.html', {})


class ChosenCityWeather(View):
        def get(self, request, **kwargs):
            user = request.user
            card = get_weather_card.get_weather_card(kwargs)['weather_card']
            #???????????????? ???????????????? ???? ???????????? ???????????? ???? id ?????? ???? request (???????????????????? ????????????????????????)
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

class BookmarkWeatherCard(View):
    def get(self, request, **kwargs):
        user = request.user
        card = get_weather_card.get_weather_card(kwargs)
        #???????????????? ???????????????? ???? ???????????? ???????????? ???? id ?????? ???? request (???????????????????? ????????????????????????)
        card.bookmark = True
        cards = WeatherCard.objects.filter(bookmard=True)
        context = {'cards': cards}
        return render(request, 'app/chosen_weather_cities.html', context)



