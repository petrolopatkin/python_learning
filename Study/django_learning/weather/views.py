from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CityForm
from .models import SavedCity
import requests


weather_descriptions = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm"
}

directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]


def get_weather(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    parameters = {
        "name": city
    }

    try:
        r = requests.get(url, params=parameters)
        r.raise_for_status()
    except requests.RequestException:
        return "error"

    print(r.status_code)
    print(r.json())

    data = r.json()

    if not data["results"]:
        return "not_found"

    else:
        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]
        location_name = data["results"][0]["name"]
        country = data["results"][0]["country"]

        print("CITY:", city)
        print("Latitude:", latitude)
        print("Longitude:", longitude)

        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_parameters = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "wind_speed_10m,"
                "wind_direction_10m,"
                "wind_gusts_10m,"
                "apparent_temperature,"
                "relative_humidity_2m,"
                "weather_code"
            )
        }

        try:
            weather_r = requests.get(
                weather_url,
                params=weather_parameters
            )
            weather_r.raise_for_status()

        except requests.RequestException:
            return "error"

        print(weather_r.status_code)

        weather_data = weather_r.json()
        print(weather_data)

        current = weather_data["current"]

        temperature = current["temperature_2m"]
        relative_humidity = current["relative_humidity_2m"]
        weather_code = current["weather_code"]

        weather_description = weather_descriptions.get(
            weather_code
        )

        wind_speed = current["wind_speed_10m"]
        wind_direction = current["wind_direction_10m"]

        direction_index = int(
            (wind_direction + 22.5) / 45
        ) % 8

        wind_direction_name = directions[direction_index]

        wind_gusts = current.get("wind_gusts_10m")
        apparent_temperature = current.get("apparent_temperature")

        weather = {
            "temperature": temperature,
            "relative_humidity": relative_humidity,
            "weather_code": weather_code,
            "wind_direction": wind_direction,
            "wind_speed": wind_speed,
            "wind_gusts": wind_gusts,
            "apparent_temperature": apparent_temperature,
            "weather_description": weather_description,
            "wind_direction_name": wind_direction_name,
            "location_name": location_name,
            "country": country
        }
        return weather


def index(request):
    cities = SavedCity.objects.all()

    city = ""
    action = ""
    weather = {}

    form = CityForm()

    if request.method == "POST":
        print("POST RECEIVED")

        action = request.POST.get("action")
        city = request.POST.get("city")

        if action == "delete":

            if SavedCity.objects.filter(
                name__iexact=city
            ).exists():

                SavedCity.objects.filter(
                    name__iexact=city
                ).delete()
                messages.success(
                    request,
                    f"{city} was deleted"
                )

                return redirect("/")

            else:
                messages.success(
                    request,
                    "City not found"
                )

        elif action == "weather":
            if not city.strip():
                messages.error(request, "Please enter a city")
                return redirect("/")
            
            weather = get_weather(city)

            if weather == "error":
                messages.error(request, "Something went wrong. Please, try again later")
                return redirect("/")

            if weather == "not_found":
                messages.error(request, "This city doesn't exist")
                return redirect("/")

        elif action == "weather-search":

            messages.success(
                request,
                f"You looked for {city}"
            )

            form = CityForm(request.POST)

            if form.is_valid():

                city = form.cleaned_data["city"].strip()

                if not SavedCity.objects.filter(
                    name__iexact=city
                ).exists():

                    SavedCity.objects.create(
                        name=city
                    )

                    messages.success(
                        request,
                        f"{city} was created"
                    )

                else:
                    messages.success(
                        request,
                        "City already saved"
                    )

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
            "form": form,
            "action": action,
            **weather
        }
    )