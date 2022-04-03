from django import forms


class SearchForm(forms.Form):
    search_input = forms.CharField(max_length=65)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search_input'].label = 'Поиск...'

    def clean_search_input(self):
        search_input = self.cleaned_data['search_input']
        if type(search_input) != str:
            raise forms.ValidationError("Введите строку в поле ввода.")
        if not search_input:
            raise forms.ValidationError("Введите в поиск название города.")
        return self.cleaned_data


