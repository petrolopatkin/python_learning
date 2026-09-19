from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CityForm
from .models import SavedCity

def index(request):
    cities = SavedCity.objects.all()
    city = ""
    action = ""

    form = CityForm()

    if request.method == 'POST':
            action = request.POST.get("action")
            city  = request.POST.get("city")
            if action == "delete":
                if SavedCity.objects.filter(name__iexact=city).exists():
                    SavedCity.objects.filter(name__iexact=city).delete()
                    messages.success(request, f"{city} was deleted")
                    return redirect("/")
                else:
                    messages.success(request, "City not found")
            elif action == "weather":
                print("WEATHER CITY: ", city)
            elif action == "weather-search":
                 message = f"You looked for {city}"
                 form = CityForm(request.POST)
                 if form.is_valid():
                        city = form.cleaned_data["city"].strip()
                        if not SavedCity.objects.filter(name__iexact=city).exists():
                            SavedCity.objects.create(name=city)
                            messages.success(request, f"{city} was created")
                        else:
                            messages.success(request, "City already saved")
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
        "action": action
        }
    )