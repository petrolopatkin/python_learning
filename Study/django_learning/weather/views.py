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

    return render(
        request,
        "weather/index.html",
        {"cities": cities}
    )