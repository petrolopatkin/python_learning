from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError, transaction
from .forms import CityForm
from .models import SavedCity
import requests
import json
import logging

logger = logging.getLogger(__name__)


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

def create_city(city_name):
    try:
        with transaction.atomic():
            city = SavedCity.objects.create(name=city_name)
    except IntegrityError:
        return None, "This city already exists"
    
    return city, None


def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    
    parameters = {
            "name": city
        }
    
    try:
            r = requests.get(url, params=parameters, timeout=10)
            r.raise_for_status()
    except requests.HTTPError:
            logger.exception("HTTP error while requesting weather")
            return "something went wrong, try again later"
    except requests.RequestException:
            logger.exception("Request exception while executing code")
            return "error"
    
    try:
            data = r.json()
    except requests.JSONDecodeError:
            logger.exception("Invalid JSON recieved from geocoding API")
            return "error"
    
    if "results" not in data:
            return "error"
    
    if not isinstance(data["results"], list):
            return "error"
        
    if not data["results"]:
            return "not_found"
    
    if not isinstance(data["results"][0], dict):
            return "error"
    
        
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    location_name = data["results"][0]["name"]
    country = data["results"][0]["country"]

    return {
         "latitude": latitude,
         "longitude": longitude,
         "location_name": location_name,
         "country": country
    }


def get_weather(city):
    coordinates = get_coordinates(city)

    if coordinates == "error":
         return "error"

    if coordinates == "not_found":
         return "not_found"

    if coordinates == "something went wrong, try again later":
         return "something went wrong, try again later"
    
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_parameters = {
            "latitude": coordinates["latitude"],
            "longitude": coordinates["longitude"],
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
                params=weather_parameters,
                timeout=10
            )
            weather_r.raise_for_status()

    except requests.RequestException:
            logger.exception("HTTP error while requesting weather")
            return "error"

    try:
            weather_data = weather_r.json()
    except requests.JSONDecodeError:
            logger.exception("Invalid JSON recieved from weather API")
            return "error"

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
            "location_name": coordinates["location_name"],
            "country": coordinates["country"]
        }
    return weather


@csrf_exempt
def cities_api(request):
    if request.method == "GET":
        cities = SavedCity.objects.all()

        data = []

        for city in cities:
            data.append({
                "id": city.id,
                "name": city.name
            })

        return JsonResponse(data, safe=False)
    elif request.method == "POST":

        try:
            body = request.body
            data = json.loads(body)
        except json.JSONDecodeError:
            return JsonResponse({
                "error": "Invalid JSON"
            }, status=400)

        if not isinstance(data, dict):
            return JsonResponse({
                "error": "JSON must be an object"
            }, status=400)

        if "name" not in data:
            return JsonResponse({
                "error": "This field is required"
            }, status=400)
        
        city_name = data["name"]

        if not isinstance(city_name, str):
            return JsonResponse({
                "error": "Incorrect name"
            }, status=400)
        
        if city_name.strip() == "":
            return JsonResponse({
                "error": "Name cannot be empty"
            }, status=400)

        city_name = city_name.strip()

        if SavedCity.objects.filter(name__iexact=city_name).exists():
            return JsonResponse({
                "error": "This city already exists"
            }, status=409)

        city_obj, error = create_city(city_name)

        if error: 
            return JsonResponse({
                "error": error
            }, status=409)

        return JsonResponse({
            "id": city_obj.id,
            "name": city_obj.name
        }, status=201)
   
    else:
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405
        )


def validate_city_name(city_name, city_id):
    if not isinstance(city_name, str):
        return None, "Incorrect name", 400

    city_name = city_name.strip()

    if not city_name:
        return None, "Name cannot be empty", 400

    if len(city_name) > 50:
        return None, "City name cannot exceed more than 50 charachters", 400 

    if SavedCity.objects.filter(name__iexact=city_name).exclude(id=city_id).exists():
        return None, "This city already exists", 409

    return city_name, None, None


def save_city_name(city_name, city):
    try:
        city.name = city_name
        city.save()
    except IntegrityError:
        return None, "This city already exists"
    return city, None


def parse_json_body(request):
    try:
        body = request.body
        data = json.loads(body)
    except json.JSONDecodeError:
        return None, "Invalid JSON", 400

    if not isinstance(data, dict):
        return None, "JSON must be an object", 400

    return data, None, None


@csrf_exempt
def city_api(request, city_id):
     if request.method == "DELETE":
            try:
                city = SavedCity.objects.get(id=city_id)
                city.delete()
            except SavedCity.DoesNotExist:
                return JsonResponse({
                    "error": "City with this id doesn't exist"
                }, status=404)
    
            return JsonResponse({
                "message": "City was deleted successfully"
            }, status=200)
     elif request.method == "PUT":
             try:
                city = SavedCity.objects.get(id=city_id)
             except SavedCity.DoesNotExist:
                return JsonResponse({
                    "error": "City with this id doesn't exist"
                }, status=404)
             
             data, error, status = parse_json_body(request)

             if error:
                return JsonResponse({
                "error": error
                }, status=status)
             
             if "name" not in data:
                return JsonResponse({
                    "error": "This field is required"
                }, status=400)
                     
             city_name, error, status = validate_city_name(
                data["name"], city_id
                )

             if error:
                return JsonResponse({
                    "error": error
                }, status=status)

             city, error = save_city_name(city_name, city)

             if error:
                 return JsonResponse({
                     "error": error
                 }, status=409)

             return JsonResponse({
                 "id": city.id,
                 "name": city.name
             }, status=200)

     elif request.method == "PATCH":
        try:
            city = SavedCity.objects.get(id=city_id)
        except SavedCity.DoesNotExist:
            return JsonResponse({
                "error": "City with this id doesn't exist"
            }, status=404)

        data, error, status = parse_json_body(request)

        if error:
            return JsonResponse({
            "error": error
            }, status=status)

        if not data or "name" not in data:
            return JsonResponse({
                "error": "No supported fields to update"
            }, status=400)

        if "name" in data:
            city_name, error, status = validate_city_name(
            data["name"], city_id
            )

            if error:
                return JsonResponse({
                "error": error
                }, status=status)

            city, error = save_city_name(city_name, city)

            if error:
                return JsonResponse({
                    "error": error
                }, status=409)

        return JsonResponse({
            "id": city.id,
            "name": city.name
        }, status=200)
        
     else:
        return JsonResponse(
            {"error": "Method not allowed"},
            status=405)


def weather_api(request, city_name):
    weather = get_weather(city_name)

    if weather == 'not_found':
        return JsonResponse({
            "error": "City not found"
        }, status=404)

    if weather == 'error':
        return JsonResponse({
            "error": "Weather Service is unavailable right now"
        }, status=502)

    return JsonResponse(weather)


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

                city_obj, error = create_city(city)

                if error:
                    messages.info(request, "City already saved")
                else:
                    messages.success(request, f"{city_obj.name} was created")

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