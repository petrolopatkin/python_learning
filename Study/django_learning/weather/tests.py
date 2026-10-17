from django.test import TestCase
from weather.models import SavedCity
import json
from unittest.mock import patch, Mock
from weather.views import get_weather
from weather.views import get_coordinates
import requests

# Create your tests here.

class CitiesAPITests(TestCase):
    @patch("weather.views.requests.get")
    def test_get_coordinates_geocoding_http_error(self, mock_get):
        fake_response = Mock()
        fake_response.raise_for_status.side_effect = requests.HTTPError("Server error")

        mock_get.return_value = fake_response

        result = get_coordinates("Paris")

        self.assertEqual(result, "something went wrong, try again later")

    @patch("weather.views.requests.get")
    def test_get_coordinates_geocoding_timeout(self, mock_get):
        mock_get.side_effect = requests.Timeout("Request timed out")

        result = get_coordinates("Paris")

        self.assertEqual(result, "error")


    @patch("weather.views.requests.get")
    def test_get_weather_forecast_http_error(self, mock_get):
        geocoding_response = Mock()

        geocoding_response.status_code = 200

        geocoding_response.json.return_value = {
            "results": [{
                "latitude": 48.8566,
                "longitude": 2.3522,
                "name": "Paris",
                "country": "France"
            }]
        }

        forecast_response = Mock()

        forecast_response.raise_for_status.side_effect = requests.HTTPError("Forecats serivce error")

        mock_get.side_effect = [geocoding_response, forecast_response]

        result = get_weather("Paris")

        self.assertEqual(result, "error")

        self.assertEqual(mock_get.call_count, 2)


    @patch("weather.views.requests.get")
    def test_get_weather_success(self, mock_get):
        geocoding_response = Mock()
    
        geocoding_response.status_code = 200
    
        geocoding_response.json.return_value = {
        "results": [{
            "latitude": 48.8566,
            "longitude": 2.3522,
            "name": "Paris",
            "country": "France"
                }]
        }
    
        forecast_response = Mock()

        forecast_response.raise_for_status.return_value = None

        forecast_response.json.return_value = {
            "current": {
                "temperature_2m": 22.5,
                "relative_humidity_2m": 60,
                "weather_code": 3,
                "wind_speed_10m": 15.0,
                "wind_direction_10m": 90,
                "wind_gusts_10m": 22.0,
                "apparent_temperature": 21.0
            }
        }

        mock_get.side_effect = [geocoding_response, forecast_response]

        result = get_weather("Paris")

        self.assertIsInstance(result, dict)

        self.assertEqual(result["location_name"], "Paris")

        self.assertEqual(result["country"], "France")

        self.assertEqual(result["temperature"], 22.5)

        self.assertEqual(result["relative_humidity"], 60)

        self.assertEqual(result["wind_direction_name"], "E")

        self.assertEqual(mock_get.call_count, 2)


    @patch("weather.views.requests.get")
    def test_get_coordinates_success(self, mock_get):
        geocoding_response = Mock()

        geocoding_response.json.return_value = {
            "results": [{
                "latitude": 48.8566,
                "longitude": 2.3522,
                "name": "Paris",
                "country": "France"
            }]
        }

        mock_get.return_value = geocoding_response

        result = get_coordinates("Paris")

        self.assertEqual(result, { 
            "latitude": 48.8566,
            "longitude": 2.3522,
            "location_name": "Paris",
            "country": "France"})

        mock_get.assert_called_once()


    @patch("weather.views.requests.get")
    def test_get_coordinates_missing_results_returns_error(self, mock_get):
        geocoding_response = Mock()

        geocoding_response.status_code = 200

        geocoding_response.json.return_value = {
            "unexpected": "data"
        }

        mock_get.return_value = geocoding_response

        result = get_coordinates("Paris")

        self.assertEqual(result, "error")

        mock_get.assert_called_once()


    @patch("weather.views.requests.get")
    def test_get_coordinates_unexpected_results_returns_error(self, mock_get):
        geocoding_response = Mock()

        geocoding_response.status_code = 200

        geocoding_response.json.return_value = {
            "results": "unexpected"
        }

        mock_get.return_value = geocoding_response

        result = get_coordinates("Paris")

        self.assertEqual(result, "error")

        mock_get.assert_called_once()


    @patch("weather.views.requests.get")
    def test_get_coordinates_results_returns_none(self, mock_get):
        geocoding_response = Mock()

        geocoding_response.status_code = 200

        geocoding_response.json.return_value = {
            "results": None
        }

        mock_get.return_value = geocoding_response

        result = get_coordinates("Paris")

        self.assertEqual(result, "error")

        mock_get.assert_called_once()


    @patch("weather.views.requests.get")
    def test_get_coordinates_results_incorrect_first_element_returns_error(self, mock_get):
        geocoding_response = Mock()

        geocoding_response.status_code = 200

        geocoding_response.json.return_value = {
            "results": ["unexpected"]
        }

        mock_get.return_value = geocoding_response

        result = get_coordinates("Paris")

        self.assertEqual(result, "error")

        mock_get.assert_called_once()


    @patch("weather.views.get_weather")
    def test_weather_api_success(self, mock_get_weather):
        mock_get_weather.return_value = {
            "temperature": 22.5
        }

        response = self.client.get("/api/weather/Paris/")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(),{
            "temperature": 22.5
        })


    @patch("weather.views.get_weather")
    def test_weather_api_city_not_found(self, mock_get_weather):
        mock_get_weather.return_value = "not_found"

        response = self.client.get("/api/weather/NonexistentCity/")

        self.assertEqual(response.status_code, 404)

        self.assertEqual(response.json(),{
            "error": "City not found"
        })


    @patch("weather.views.get_weather")
    def test_weather_api_service_unavailable(self, mock_get_weather):
        mock_get_weather.return_value = "error"

        response = self.client.get("/api/weather/Paris/")

        self.assertEqual(response.status_code, 502)

        self.assertEqual(response.json(), {
            "error": "Weather Service is unavailable right now"
        })
        

    def test_get_cities_returns_saved_cities(self):
        city = SavedCity.objects.create(name="Prague")

        response = self.client.get("/api/cities/")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response["Content-Type"], "application/json")

        self.assertEqual(
            response.json(),
                [{"id": city.id, "name": "Prague"}]
        )


    def test_post_cities_creates_city(self):
        response = self.client.post("/api/cities/", data=json.dumps({
            "name": "Berlin"
        }), content_type="application/json")

        self.assertEqual(response.status_code, 201)

        self.assertEqual(response["Content-Type"], "application/json")

        self.assertEqual(SavedCity.objects.filter(name="Berlin").count(), 1)

        self.assertEqual(response.json()["name"], "Berlin")


    def test_post_cities_without_name_returns_400(self):
        cities_before = SavedCity.objects.count()

        response = self.client.post("/api/cities/", data=json.dumps({}), 
        content_type="application/json")

        self.assertEqual(response.status_code, 400)

        self.assertEqual(response["Content-Type"], "application/json")

        self.assertEqual(SavedCity.objects.count(), cities_before)


    def test_post_cities_duplicates_returns_409(self):
        city = SavedCity.objects.create(name="Berlin")

        response = self.client.post("/api/cities/", data=json.dumps({
            "name": city.name
        }), content_type="application/json")

        self.assertEqual(response.status_code, 409)

        self.assertEqual(response["Content-Type"], "application/json")

        self.assertEqual(SavedCity.objects.filter(name="Berlin").count(), 1)


    def test_post_cities_whitespace_name_returns_400(self):
        cities_before = SavedCity.objects.count()

        response = self.client.post("/api/cities/", data=json.dumps({
            "name": "    "
        }), content_type="application/json")

        self.assertEqual(response.status_code, 400)

        self.assertEqual(response["Content-Type"], "application/json")

        self.assertEqual(SavedCity.objects.count(), cities_before)


    def test_post_with_incorrect_json_returns_400(self):
        cities_before = SavedCity.objects.count()

        response = self.client.post("/api/cities/", data="{invalid JSON", content_type="application/json")

        self.assertEqual(response.status_code, 400)
        
        self.assertEqual(response["Content-Type"], "application/json")

        self.assertEqual(SavedCity.objects.count(), cities_before)


    def test_post_incorrect_type_of_data_returns_400(self):
        cities_before = SavedCity.objects.count()
        
        response = self.client.post("/api/cities/", data=json.dumps({
            "name": 123
        }), content_type="application/json")
        
        self.assertEqual(response.status_code, 400)
                
        self.assertEqual(response["Content-Type"], "application/json")
        
        self.assertEqual(SavedCity.objects.count(), cities_before)


    def test_delete_cities_returns_200(self):
        city = SavedCity.objects.create(name="Vienna")

        response = self.client.delete(f"/api/cities/{city.id}/")


        self.assertEqual(response.status_code, 200)

        self.assertEqual(response["Content-Type"], "application/json")

        self.assertFalse(SavedCity.objects.filter(id=city.id).exists())


    def test_delete_nonexistent_city_404(self):
        response = self.client.delete("/api/cities/99999/")

        self.assertEqual(response.status_code, 404)

        self.assertEqual(response["Content-Type"], "application/json")


    def test_put_city_returns_200(self):
        city = SavedCity.objects.create(name="Vienna")

        response = self.client.put(f"/api/cities/{city.id}/", data=json.dumps({
            "name": "Vienna Updated"
        }), content_type="application/json")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response["Content-Type"], "application/json")

        self.assertTrue(SavedCity.objects.filter(name="Vienna Updated").exists())


    def test_put_nonexistent_city_returns_404(self):
        response = self.client.put("/api/cities/999999/", data=json.dumps({
            "name": "Vienna Updated"
        }), content_type="application/json")

        self.assertEqual(response.status_code, 404)

        self.assertEqual(response["Content-Type"], "application/json")


    def test_put_duplicate_city_returns_409(self):
        city1 = SavedCity.objects.create(name="Vienna")
        city2 = SavedCity.objects.create(name="Prague")

        response = self.client.put(f"/api/cities/{city1.id}/", data=json.dumps({
            "name": "Prague"
        }), content_type="application/json")

        self.assertEqual(response.status_code, 409)
        
        self.assertEqual(response["Content-Type"], "application/json")

        self.assertTrue(SavedCity.objects.filter(name="Vienna").exists())

        self.assertTrue(SavedCity.objects.filter(name="Prague").exists())

        self.assertEqual(SavedCity.objects.count(), 2)


    def test_put_empty_name_returns_400(self):
        city = SavedCity.objects.create(name="Vienna")

        response = self.client.put(f"/api/cities/{city.id}/", data=json.dumps({}), content_type="application/json")

        self.assertEqual(response.status_code, 400)

        self.assertEqual(response["Content-Type"], "application/json")

        self.assertEqual(response.json(), {
            "error": "This field is required"
        })

        self.assertEqual(SavedCity.objects.get(id=city.id).name, "Vienna")


    def test_patch_change_name_returns_200(self):
        city = SavedCity.objects.create(name="Vienna")

        response = self.client.patch(f"/api/cities/{city.id}/", data=json.dumps({
            "name": "Prague"
        }), content_type="application/json")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response["Content-Type"], "application/json")

        self.assertTrue(SavedCity.objects.filter(id=city.id, name="Prague").exists())


    def test_patch_invalid_json_returns_400(self):
        city = SavedCity.objects.create(name="Vienna")

        response = self.client.patch(f"/api/cities/{city.id}/", data="{invalid JSON", content_type="application/json")

        self.assertEqual(response.status_code, 400)

        self.assertEqual(response["Content-Type"], "application/json")

        self.assertTrue(SavedCity.objects.filter(id=city.id, name="Vienna").exists())


    def test_patch_duplicate_city_returns_409(self):
        city1 = SavedCity.objects.create(name="Vienna")
        city2 = SavedCity.objects.create(name="Prague")
    
        response = self.client.patch(f"/api/cities/{city1.id}/", data=json.dumps({
                "name": "Prague"
            }), content_type="application/json")
    
        self.assertEqual(response.status_code, 409)
            
        self.assertEqual(response["Content-Type"], "application/json")
    
        self.assertTrue(SavedCity.objects.filter(name="Vienna").exists())
    
        self.assertTrue(SavedCity.objects.filter(name="Prague").exists())
    
        self.assertEqual(SavedCity.objects.count(), 2)


    def test_patch_empty_json_returns_400(self):
        city = SavedCity.objects.create(name="Vienna")

        response = self.client.patch(f"/api/cities/{city.id}/", data=json.dumps({}), content_type="application/json")

        self.assertEqual(response.status_code, 400)

        self.assertEqual(response["Content-Type"], "application/json")

        self.assertEqual(response.json(), {
            "error": "No supported fields to update"
        })

        self.assertTrue(SavedCity.objects.filter(name="Vienna").exists())


    def test_patch_unknown_field_returns_400(self):
        city = SavedCity.objects.create(name="Vienna")

        response = self.client.patch(f"/api/cities/{city.id}/", data=json.dumps({
            "country": "France"
        }), content_type="application/json")

        self.assertEqual(response.status_code, 400)

        self.assertEqual(response["Content-Type"], "application/json")

        self.assertEqual(response.json(), {
            "error": "No supported fields to update"
        })

        self.assertTrue(SavedCity.objects.filter(name="Vienna").exists())


    def test_patch_incorrect_name_returns_400(self):
        city = SavedCity.objects.create(name="Vienna")

        response = self.client.patch(f"/api/cities/{city.id}/", data=json.dumps({
            "name": 123
        }), content_type="application/json")

        self.assertEqual(response.status_code, 400)

        self.assertEqual(response["Content-Type"], "application/json")

        self.assertEqual(response.json(), {
            "error": "Incorrect name"
        })

        self.assertEqual(SavedCity.objects.get(id=city.id).name, "Vienna")


    def test_patch_nonexistent_city_returns_404(self):
        response = self.client.patch("/api/cities/99999/", data=json.dumps({
            "name": "Prague"
        }), content_type="application/json")

        self.assertEqual(response.status_code, 404)

        self.assertEqual(response["Content-Type"], "application/json")