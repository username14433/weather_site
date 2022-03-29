def filter_weather_data(request):
    query = request.GET.get('q')
    city = query.strip(' ')[0]
    country = query.strip(' ')[2]
    return {'city': city, 'country': country}

