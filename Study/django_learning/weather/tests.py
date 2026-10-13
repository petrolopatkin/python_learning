from django.test import TestCase
from weather.models import SavedCity
import json

# Create your tests here.

class CitiesAPITests(TestCase):

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

        self.assertTrue(SavedCity.objects.filter(name="Berlin").exists())


    def test_post_cities_without_name_returns_400(self):
        response = self.client.post("/api/cities/", data=json.dumps({}), 
        content_type="application/json")

        self.assertEqual(response.status_code, 400)

        self.assertEqual(response["Content-Type"], "application/json")


    def test_post_cities_duplicates_returns_409(self):
        city = SavedCity.objects.create(name="Berlin")

        response = self.client.post("/api/cities/", data=json.dumps({
            "name": city.name
        }), content_type="aplication/json")

        self.assertEqual(response.status_code, 409)

        self.assertEqual(response["Content-Type"], "application/json")

        self.assertEqual(SavedCity.objects.filter(name="Berlin").count(), 1)


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