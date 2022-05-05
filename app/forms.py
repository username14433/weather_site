import string

from django import forms


class SearchForm(forms.Form):
    city = forms.CharField(max_length=65)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].label = 'Поиск...'

    def clean_city(self):
        city = self.cleaned_data['city']

        for symbol in city:
            if str(symbol) in string.digits:
                raise forms.ValidationError("Назывние города не может содержать числа.")
        if not city:
            raise forms.ValidationError("Введите в поиск название города.")
        return self.cleaned_data
