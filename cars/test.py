from rest_framework import status
from rest_framework.test import APITestCase


class CarTestCase(APITestCase):
    def test_car(self):
        data = {"make": "Opel", "model": "Ampera"}
        response = self.client.post("/cars", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CarsListTestCase(APITestCase):
    def test_cars_list(self):
        response = self.client.get("/cars")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTestCase(APITestCase):
    def test_car(self):
        response = self.client.delete("/delete/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RateTestCase(APITestCase):
    def test_car(self):
        data = {"make": 5, "model": 1}
        response = self.client.post("/rate", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PopularTestCase(APITestCase):
    def test_car(self):
        response = self.client.get("/popular")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
