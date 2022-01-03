from django.contrib.sites import requests
from django.http import JsonResponse, HttpResponse
from rest_framework import views
from rest_framework.response import Response
from django.db.models import Avg
import requests

from .serializers import CarSerializer, RateSerializer
from .models import Car, Rate


class CreateCarView(views.APIView):
    def get(self, request) -> HttpResponse or JsonResponse:
        queryset_of_cars = Car.objects.all().values()
        if not queryset_of_cars:
            return HttpResponse("Database is empty, please send some data to the database.")
        else:
            list_of_cars = []
            for car in queryset_of_cars:
                rate = Rate.objects.filter(cars=car['id']).aggregate(Avg('rate'))
                dict_car = {
                    "id": car['id'],
                    "make": car['make'],
                    "model": car['model'],
                    "avg_rating": rate['rate__avg'],
                }
                list_of_cars.append(dict_car)
            return JsonResponse(list_of_cars, safe=False)

    def post(self, request) -> HttpResponse or Response:
        dict_car_id = request.data
        car_make = dict_car_id['make']
        car_model = dict_car_id['model']
        response_from_api = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{car_make}?format=json")
        data_from_api = response_from_api.json()
        result_from_api = data_from_api['Results']
        if not any(a['Model_Name'] == f"{car_model}" for a in result_from_api):
            return HttpResponse("Please, provide correct data.")
        else:
            serializer = CarSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class WelcomeView(views.APIView):
    def get(self, request) -> HttpResponse:
        return HttpResponse("Welcome on my application Cars_REST_API.")


class DeleteCarView(views.APIView):
    def delete(self, request, car_id: int) -> HttpResponse:
        try:
            obj = Car.objects.get(id=car_id)
            obj.delete()
            return HttpResponse("Car was deleted successfully.")
        except Car.DoesNotExist:
            return HttpResponse("Please provide correct data, car with given id doesn't exist.")


class CreateRateView(views.APIView):
    def post(self, request) -> Response or HttpResponse:
        try:
            serializer = RateSerializer(data=request.data)
            serializer.is_valid(raise_exception=False)
            serializer.save()
            return Response(serializer.data)
        except AssertionError:
            return HttpResponse("Please provide correct data, rate is not between 1 and 5 or car with given id doesn't exist.")


class PopularCarsView(views.APIView):
    def get(self, request) -> JsonResponse or HttpResponse:
        try:
            queryset_of_cars = Car.objects.all().values()
            list_of_cars = []
            for car in queryset_of_cars:
                rate = Rate.objects.filter(cars=car['id']).count()
                dict_car = {
                    "id": car['id'],
                    "make": car['make'],
                    "model": car['model'],
                    "rates_number": rate,
                }
                list_of_cars.append(dict_car)
                sorted_list_of_cars = sorted(list_of_cars, key=lambda x: -x['rates_number'])
                top_list_of_cars = sorted_list_of_cars[0:2]
            return JsonResponse(top_list_of_cars, safe=False)
        except UnboundLocalError:
            return HttpResponse("Database is empty, please send some data to the database.")
