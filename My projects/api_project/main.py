from weather import get_coordinates
from weather import get_weather
from weather import save_city
from weather import load_saved_cities
from weather import get_weather_for_saved_cities
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
            result = get_coordinates()
            if result:
                  city, latitude, longitude = result
                  print(f"Latitude: {latitude}")
                  print(f"Longitude: {longitude}")
            save_city_ask = input("You want to save this city? ").lower()
            if save_city_ask == "y":
                        save_city(city, latitude, longitude)
                        print("City was successfully saved!")
            else:
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
""")
            saved_command = int(input("> "))
            if saved_command == 1:
                  load_saved_cities()
            elif saved_command == 2:
                  result =  get_weather_for_saved_cities()
                  if result: 
                         city, latitude, longitude = result
                         get_weather(city, latitude, longitude)
      elif command == 4:
            break
      else:
            print("Invalid command, try again")