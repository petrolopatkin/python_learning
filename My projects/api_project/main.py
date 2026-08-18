import requests
pr = {
    "name" : "Prešov"
}
r = requests.get('https://geocoding-api.open-meteo.com/v1/search', params=pr)

print(r.status_code)
#print(r.json())
data = r.json()
results = data["results"][0]
print(results)
latitude = data["results"][0]["latitude"]
longitude = data["results"][0]["longitude"]
print(latitude)
print(longitude)

pr2 = {
    "name": "Prešov",
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m"
}
r = requests.get('https://api.open-meteo.com/v1/forecast', params=pr2)
print(r.status_code)
#print(r.json())
weather_data = r.json()
temperature = weather_data["current"]["temperature_2m"]
print(temperature)