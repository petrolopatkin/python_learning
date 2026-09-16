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
        action = request.POST.get("action")
        city  = request.POST.get("city")
        if action == "delete":
            if city in cities:
                cities.remove(city)
                request.session["cities"] = cities
            else:
                print("Incorrect deletion")
        elif action == "weather":
            print("WEATHER CITY: ", city)

        if form.is_valid():
            city = form.cleaned_data["city"].strip()

            if not any(saved_city.lower() == city.lower() for saved_city in cities):
                cities.append(city).lower()
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