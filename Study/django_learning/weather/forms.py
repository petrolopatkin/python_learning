from django import forms

class CityForm(forms.Form):
    city = forms.CharField(max_length=50, 
    label= "",
    widget=forms.TextInput(attrs={
        "class": "search__input",
        "placeholder": "Enter a city: "
    }))