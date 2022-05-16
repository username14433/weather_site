import string

from django import forms

from .models import User


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

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.PasswordInput()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = "Введите свой username: "
        self.fields['password'].label = "Введите пароль: "

    def clean(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)
        if user:
            raise forms.ValidationError('Такое имя уже существует!')
        return username
