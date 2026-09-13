from django.shortcuts import render


def index(request):
    cities = [
        "Prešov",
        "Košice",
        "Kyiv",
        "Lviv",
        "Bratislava",
        "London"
    ]

    city = ""

    if request.method == 'POST':
        city = request.POST.get("city")
        if city:
            cities.append(city)
        else:
            print("You entered invalid city, try again")

    return render(
        request,
        "weather/index.html",
        {
        "cities": cities,
        "city": city
        }
    )