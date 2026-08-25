import requests
import json
weather_codes = {
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
def get_coordinates():
    city = input("Name a city: ")
    pr = {
        "name": city
    }
    r = make_api_request('https://geocoding-api.open-meteo.com/v1/search', params=pr)
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
    r = make_api_request('https://api.open-meteo.com/v1/forecast', params=pr2)
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
    weather_description = weather_codes[weather_code]
    print(f"""---------{city}----------
Temperature: {temperature}°C
Feels like: {apparent_temperature}°C
Humidity: {relative_humididty}%
Wind Speed: {wind_speed}km/h
Wind Direction: {wind_direction}
Wind Gusts: {wind_gusts}km/h
Weather code: {weather_code} - {weather_description}
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
     return saved_cities       


def get_weather_for_saved_cities():
        while True:
         with open("My projects/api_project/cities.json", "r") as f:
          saved_cities = json.load(f)
         for number, city in enumerate(saved_cities, start= 1):
          print(f"{number}. {city['name']}")
         try:
          choice = int(input("Choose a city: ")) 
          index = choice - 1
          selected_city = saved_cities[index]
         except ValueError:
            print("Invalid value, try again")
            continue
         except IndexError:
            print("Incorrect index, try again")
            continue
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
    r = make_api_request('https://api.open-meteo.com/v1/forecast', params=pr3)
    #print(r.status_code)
    #print(r.json())
    forecast_data = r.json()
    max_temperature = forecast_data["daily"]["temperature_2m_max"][0]
    min_temperature = forecast_data["daily"]["temperature_2m_min"][0]
    weather_code = forecast_data["daily"]["weather_code"][0]
    weather_description = weather_codes[weather_code]
    print(f"""---------{city}----------
Max Temperature: {max_temperature}°C
Min Temperature: {min_temperature}°C
Weather Code: {weather_code} - {weather_description}
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
    r = make_api_request('https://api.open-meteo.com/v1/forecast', params=pr4)
    seven_forecast_data = r.json()
    date = seven_forecast_data["daily"]["time"]
    max_temperature = seven_forecast_data["daily"]["temperature_2m_max"]
    min_temperature = seven_forecast_data["daily"]["temperature_2m_min"]
    weather_code = seven_forecast_data["daily"]["weather_code"]
    for i in range(len(date)):
     weather_description = weather_codes[weather_code[i]]
     print(f"""---------{city}----------
    Date: {date[i]}
    Max Temperature: {max_temperature[i]}
    Min Temperature: {min_temperature[i]}
    Weather Code: {weather_code[i]} - {weather_description}
-------------------------""")


def make_api_request(url, params):
   try:
      r = requests.get(url, params=params, timeout=5)
      r.raise_for_status()
      return r
   except requests.ConnectionError:
     print("You aren't connected now. Check your connection and try again")
   except requests.Timeout:
     print("Server is not responding now, try again later")
   except requests.HTTPError:
     print("Something went wrong, try again")


def get_hourly_forecast(city, latitude, longitude):
   pr5 = {
      "name": city,
      "latitude": latitude,
      "longitude": longitude,
      "hourly": "temperature_2m,wind_speed_10m,wind_direction_10m,wind_gusts_10m,apparent_temperature,relative_humidity_2m,weather_code",
      "forecast_hours": 24
   }
   r = make_api_request('https://api.open-meteo.com/v1/forecast', params=pr5)
   hourly_data = r.json()
   hour = hourly_data["hourly"]["time"]
   temperature = hourly_data["hourly"]["temperature_2m"]
   wind_speed = hourly_data["hourly"]["wind_speed_10m"]
   wind_direction = hourly_data["hourly"]["wind_direction_10m"]
   wind_gusts = hourly_data["hourly"]["wind_gusts_10m"]
   apparent_temperature = hourly_data["hourly"]["apparent_temperature"]
   relative_humidity = hourly_data["hourly"]["relative_humidity_2m"]
   weather_code = hourly_data["hourly"]["weather_code"]

   for i in range(len(hour)):
       weather_description = weather_codes[weather_code[i]]
       print(f"""---------{city}----------
Time: {hour[i]}
Temperature: {temperature[i]}°C
Feels like: {apparent_temperature[i]}°C
Humidity: {relative_humidity[i]}%
Wind Speed: {wind_speed[i]}km/h
Wind Direction: {wind_direction[i]}
Wind Gusts: {wind_gusts[i]}km/h
Weather code: {weather_code[i]} - {weather_description}
-------------------------""")


def get_weather_for_specific_hour(city, latitude, longitude):
     pr5 = {
          "name": city,
          "latitude": latitude,
          "longitude": longitude,
          "hourly": "temperature_2m,wind_speed_10m,wind_direction_10m,wind_gusts_10m,apparent_temperature,relative_humidity_2m,weather_code",
          "forecast_hours": 24
       }
     r = make_api_request('https://api.open-meteo.com/v1/forecast', params=pr5)
     hourly_data = r.json()
     hour = hourly_data["hourly"]["time"]
     temperature = hourly_data["hourly"]["temperature_2m"]
     wind_speed = hourly_data["hourly"]["wind_speed_10m"]
     wind_direction = hourly_data["hourly"]["wind_direction_10m"]
     wind_gusts = hourly_data["hourly"]["wind_gusts_10m"]
     apparent_temperature = hourly_data["hourly"]["apparent_temperature"]
     relative_humididty = hourly_data["hourly"]["relative_humidity_2m"]
     weather_code = hourly_data["hourly"]["weather_code"]
     for number, hour in enumerate(hour, start=1):
        print(f"{number}. {hour}")
     while True:
      try:
        hour_choice = int(input("Choose an hour: "))
        index2 = hour_choice - 1
      except ValueError:
         print("Invalid value, try again")
         continue
      break
     selected_hour = hour[index2]
     selected_temperature = temperature[index2]
     selected_wind_speed =  wind_speed[index2]
     selected_wind_direction =  wind_direction[index2]
     selected_wind_gusts =  wind_gusts[index2]
     selected_apparent_temperature =  apparent_temperature[index2]
     selected_relative_humidity =  relative_humididty[index2]
     selected_weather_code = weather_code[index2]
     selected_weather_description = weather_codes[selected_weather_code]
     print(f"""---------{city}----------
Time: {selected_hour}
Temperature: {selected_temperature}°C
Feels like: {selected_apparent_temperature}°C
Humidity: {selected_relative_humidity}%
Wind Speed: {selected_wind_speed}km/h
Wind Direction: {selected_wind_direction}
Wind Gusts: {selected_wind_gusts}km/h
Weather code: {selected_weather_code} - {selected_weather_description}
-------------------------""")


def delete_saved_city():
   saved_cities = load_saved_cities()
   for number, city in enumerate(saved_cities, start=1):
      print(f"{number}. {city['name']}")
   while True:
      try:
         choice = int(input("Which city you want to delete? "))
      except ValueError:
         print("Incorrect value, try again")
         continue
      except IndexError:
         print("Incorrect index, try again")
         continue
      if choice < 1 or choice > len(saved_cities):
         print("This number doesn't exist yet")
      else:
         warning_message = input("Are you sure you want ot delete this city? ").lower()
         if warning_message == "y":
            saved_cities.pop(choice - 1)
            with open("My projects/api_project/cities.json", "w") as f:
               json.dump(saved_cities, f, indent=2)
            print("City was successfully deleted")
            break
         elif warning_message == "n":
            print("You have cancelled deletion")
            return
         else:
            print("You picked incorrect answer, try again")