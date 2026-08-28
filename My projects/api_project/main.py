from weather import get_coordinates
from weather import get_weather
from weather import save_city
from weather import load_saved_cities
from weather import get_weather_for_saved_cities
from weather import get_todays_forecast
from weather import get_forecast_for_seven_days
from weather import get_hourly_forecast
from weather import get_weather_for_specific_hour
from weather import delete_saved_city
result = None
while True:
      print("""
1. Get coordinates
2. Get Weather
3. Saved cities
4. Exit""")
      try:
            command = int(input("> "))
      except ValueError:
            print("Invalid value, try again")
            continue
      if command == 1:
            city = input("Name a city: ")
            result = get_coordinates(city)
            if result:
                  city, latitude, longitude = result
                  print(f"Latitude: {latitude}")
                  print(f"Longitude: {longitude}")
            save_city_ask = input("You want to save this city? ").lower()
            if save_city_ask == "y":
                        save_city(city, latitude, longitude)
                        print("City was successfully saved!")
            else:
                        print("You cancelled the deletion")
                        continue
      elif command == 2: 
            if result:
                  city, latitude, longitude = result
                  get_weather(city, latitude, longitude)
            else:
                  print("First get the coordinates")
      elif command == 3: 
            print("""
1. Show saved cities
2. Get weather for saved city
3. Get today's forecast
4. Get forecast for 7 days
5. Get hourly forecast
6. Get weather for selected hour
7. Delete saved city
""")
            try:
             saved_command = int(input("> "))
            except ValueError:
                   print("Invalid value, try again")
                   continue
            if saved_command == 1:
                  load_saved_cities()
            elif saved_command == 2:
                  result =  get_weather_for_saved_cities()
                  if result: 
                         city, latitude, longitude = result
                         get_weather(city, latitude, longitude)
            elif saved_command == 3:
                   result = get_weather_for_saved_cities()
                   if result:
                          city, latitude, longitude = result
                          get_todays_forecast(city, latitude, longitude) 
            elif saved_command == 4:
                   result = get_weather_for_saved_cities()
                   if result:
                          city, latitude, longitude = result
                          get_forecast_for_seven_days(city, latitude, longitude)
            elif saved_command == 5:
                   result = get_weather_for_saved_cities()
                   if result:
                          city, latitude, longitude = result
                          get_hourly_forecast(city, latitude, longitude) 
            elif saved_command == 6:
                   result = get_weather_for_saved_cities()
                   if result:
                          city, latitude, longitude = result
                          get_weather_for_specific_hour(city, latitude, longitude)      
            elif saved_command == 7:
                   delete_saved_city()
      elif command == 4:
            break
      else:
            print("Invalid command, try again")