from django.http import JsonResponse
from rest_framework import views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Avg

from .serializers import CarSerializer, RateSerializer
from .models import Car, Rate


class CreateCarView(views.APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CarView(views.APIView):
    def post(self, request):
        dict_id = request.data
        car_id = dict_id['car_id']
        list_of_cars = Car.objects.filter(id=car_id).values()
        take_id = list_of_cars[0]['id']
        take_make = list_of_cars[0]['make']
        take_model = list_of_cars[0]['model']
        dict_rate_average = Rate.objects.filter(cars=car_id).aggregate(Avg('rate'))
        rate_average = dict_rate_average['rate__avg']
        make_dict = {
            "id": take_id,
            "make": take_make,
            "model": take_model,
            "avg_rating": rate_average
        }
        return Response(make_dict)


class ListOfCarsView(views.APIView):
    def get(self, request):
        list_of_cars = Car.objects.all()
        cars_serializer = CarSerializer(list_of_cars, many=True)
        print(cars_serializer)
        return JsonResponse(cars_serializer.data, safe=False)


class DeleteCarView(views.APIView):
    def delete(self, request):
        dict_id = request.data
        car_id = dict_id['car_id']
        obj = get_object_or_404(Car, id=car_id)
        obj.delete()
        return JsonResponse("Car was deleted successfully.", safe=False)


class CreateRateView(views.APIView):
    def post(self, request):
        serializer = RateSerializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ListOfRatesView(views.APIView):
    def get(self, request):
        list_of_rates = Rate.objects.all()
        rates_serializer = RateSerializer(list_of_rates, many=True)
        print(rates_serializer)
        return JsonResponse(rates_serializer.data, safe=False)


class RateView(views.APIView):
    def post(self, request):
        dict_of_data = request.data
        cars_id = dict_of_data['cars']
        list_of_rates = Rate.objects.filter(cars=cars_id)
        rates_serializer = RateSerializer(list_of_rates, many=True)
        return JsonResponse(rates_serializer.data, safe=False)
