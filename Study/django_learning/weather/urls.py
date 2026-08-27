from django.urls import path
from . import views
urlpatterns = [
    path(("weather/", include("weather.urls")), views.home, name = "home"),
]