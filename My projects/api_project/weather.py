import requests
import json
def get_coordinates():
    city = input("Name a city: ")
    pr = {
        "name": city
    }
    r = requests.get('https://geocoding-api.open-meteo.com/v1/search', params=pr)

    #print(r.status_code)
    #print(r.json())
    data = r.json()
    if not data["results"]:
        print("City not found")
        return None
    else:
        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]
        return city, latitude, longitude


def get_weather(city, latitude, longitude):
    pr2 = {
        "name": city,
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,wind_direction_10m,wind_gusts_10m,apparent_temperature,relative_humidity_2m,weather_code"
    }
    r = requests.get('https://api.open-meteo.com/v1/forecast', params=pr2)
    #print(r.status_code)
    #print(r.json())
    weather_data = r.json()
    temperature = weather_data["current"]["temperature_2m"]
    wind_speed = weather_data["current"]["wind_speed_10m"]
    wind_direction = weather_data["current"]["wind_direction_10m"]
    wind_gusts = weather_data["current"]["wind_gusts_10m"]
    apparent_temperature = weather_data["current"]["apparent_temperature"]
    relative_humididty = weather_data["current"]["relative_humidity_2m"]
    weather_code = weather_data["current"]["weather_code"]
    print(f"""---------{city}----------
Temperature: {temperature}°C
Feels like: {apparent_temperature}°C
Humidity: {relative_humididty}%
Wind Speed: {wind_speed}km/h
Wind Direction: {wind_direction}
Wind Gusts: {wind_gusts}km/h
Weather code: {weather_code}
-------------------------""")


def save_city(city, latitude, longitude):
    with open("My projects/api_project/cities.json", "r") as f:
        cities = json.load(f)
    saved_cities = {
            "name": city,
            "latitude": latitude,
            "longitude": longitude
        }
    cities.append(saved_cities)
    with open("My projects/api_project/cities.json", "w") as f:
        json.dump(cities, f, indent=2)


def load_saved_cities():
     with open("My projects/api_project/cities.json", "r") as f:
         saved_cities = json.load(f)
     for number, city in enumerate(saved_cities, start= 1):
        print(f"{number}. {city['name']}")         


def get_weather_for_saved_cities():
        with open("My projects/api_project/cities.json", "r") as f:
         saved_cities = json.load(f)
        for number, city in enumerate(saved_cities, start= 1):
         print(f"{number}. {city['name']}")
        choice = int(input("Choose a city: ")) 
        index = choice - 1
        selected_city = saved_cities[index]
        return selected_city["name"], selected_city["latitude"], selected_city["longitude"]


def get_todays_forecast(city, latitude, longitude):
    pr3 = {
        "name": city,
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min,weather_code",
        "forecast_days": 1,
        "timezone": "auto"
    }
    r = requests.get('https://api.open-meteo.com/v1/forecast', params=pr3)
    #print(r.status_code)
    #print(r.json())
    forecast_data = r.json()
    max_temperature = forecast_data["daily"]["temperature_2m_max"][0]
    min_temperature = forecast_data["daily"]["temperature_2m_min"][0]
    weather_code = forecast_data["daily"]["weather_code"][0]
    print(f"""---------{city}----------
Max Temperature: {max_temperature}°C
Min Temperature: {min_temperature}°C
Weather Code: {weather_code}
-------------------------""")


def get_forecast_for_seven_days(city, latitude, longitude):
    pr4 = {
            "name": city,
            "latitude": latitude,
            "longitude": longitude,
            "daily": "temperature_2m_max,temperature_2m_min,weather_code",
            "forecast_days": 7,
            "timezone": "auto"
    }
    r = requests.get('https://api.open-meteo.com/v1/forecast', params=pr4)
    seven_forecast_data = r.json()
    date = seven_forecast_data["daily"]["time"]
    max_temperature = seven_forecast_data["daily"]["temperature_2m_max"]
    min_temperature = seven_forecast_data["daily"]["temperature_2m_min"]
    weather_code = seven_forecast_data["daily"]["weather_code"]
    for i in range(len(date)):
        print(f"""---------{city}----------
    Date: {date[i]}
    Max Temperature: {max_temperature[i]}
    Min Temperature: {min_temperature[i]}
    Weather Code: {weather_code[i]}
-------------------------""")