# practice after my API project in Python
#Task1 functions + lists
def get_even_numbers():
    choice_numbers = input("Pick a group of numbers: ").split()
    numbers = [int(num) for num in choice_numbers]
    even_num = [num for num in numbers if num % 2 == 0]
    print(even_num)

get_even_numbers()

#Task 2 dictionary + try/except
def city():
    cities = {
    "Presov": 50,
    "Kosice": 100,
    "Kiev": 150
}
    choice = input("Enter a name of the city: ")
    if choice not in cities:
        print("This city isn't in the dictionary")
    else:
       print(choice, cities[choice])

city()
#Task 3
import requests
def get_data():
    try:
     r = requests.get('https://open.spotify.com/', timeout=5)
     r.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("Something is wrong with your connection. Check your connection and try again")
        return
    except requests.exceptions.ConnectTimeout:
        print("Something went wrong. Try ro refresh the page")
        return
    except requests.HTTPError:
        print("Something went wrong with our page. Try again later")
        return
    print(r.status_code)
    print(r.json())


get_data()