def filter_weather_data(request):
    query = request.GET.get('q')
    city = query.strip(' ')[0]
    country = query.strip(' ')[2]
    return {'city': city, 'country': country}

# def func():
#     x = 5
#     b = 7
#     return {'x': x, 'b': b}
# print(func()['x'])
