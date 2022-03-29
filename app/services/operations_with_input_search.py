def get_search_input(request):
    search_input = request.POST.get('q')
    return search_input