from weather import get_coordinates
from weather import get_weather
result = None
while True:
      print("""
1. Get coordinates
2. Get Weather
3. Exit""")
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
      elif command == 2: 
            if result:
                  city, latitude, longitude = result
                  get_weather(city, latitude, longitude)
            else:
                  print("First get the coordinates")
      elif command == 3: 
            break
      else:
            print("Invalid command, try again")