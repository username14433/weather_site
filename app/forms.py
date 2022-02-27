from django import forms
from .models import City, WeatherCard

class SearchForm(forms.Form):
    search_input = forms.CharField(max_length=65)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search_input'].label = 'Поиск...'
    def clean_search_input(self):
        search_input = self.cleaned_data['search_input']
        return self.cleaned_data