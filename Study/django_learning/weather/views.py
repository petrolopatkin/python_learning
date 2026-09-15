from django.shortcuts import render
from .forms import CityForm


def index(request):
    default_cities = [
        "Prešov",
        "Košice",
        "Kyiv",
        "Lviv",
        "Bratislava",
        "London"
    ]

    cities = request.session.get("cities", default_cities)
    city = ""

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            city = form.cleaned_data["city"].strip()

            if city not in cities:
                cities.append(city)
                request.session["cities"] = cities
        else:
            print("You entered invalid city")
    else:
        form = CityForm()

    return render(
        request,
        "weather/index.html",
        {
        "cities": cities,
        "city": city,
        "form": form
        }
    )