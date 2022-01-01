from django.http import JsonResponse
from rest_framework import views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Avg

from .serializers import CarSerializer, RateSerializer
from .models import Car, Rate


class CreateCarView(views.APIView):
    def get(self, request):
        queryset_of_cars = Car.objects.all().values()
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

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# class FindCarView(views.APIView):
#     def post(self, request):
#         dict_car_id = request.data
#         car_id = dict_car_id['id']
#         find_car = Car.objects.filter(id=car_id).values()
#         car_make = find_car[0]['make']
#         car_model = find_car[0]['model']
#         dict_car = {
#             "make": car_make,
#             "model": car_model
#         }
#         return JsonResponse(dict_car)


class WelcomeView(views.APIView):
    def get(self, request):
        return JsonResponse("Welcome on my APP", safe=False)


class DeleteCarView(views.APIView):
    def delete(self, request, car_id):
        obj = get_object_or_404(Car, id=car_id)
        obj.delete()
        return JsonResponse("Car was deleted successfully.", safe=False)


class CreateRateView(views.APIView):
    def post(self, request):
        serializer = RateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# class ListOfRatesView(views.APIView):
#     def get(self, request):
#         list_of_rates = Rate.objects.all()
#         rates_serializer = RateSerializer(list_of_rates, many=True)
#         return JsonResponse(rates_serializer.data, safe=False)


# class FindRateView(views.APIView):
#     def post(self, request):
#         dict_of_data = request.data
#         rate_id = dict_of_data['id']
#         find_rate = Rate.objects.filter(id=rate_id).values()
#         my_rate = Rate.objects.get(id=rate_id)
#         my_car = my_rate.cars.all().values()
#         car_id = my_car[0]['id']
#         rate = find_rate[0]['rate']
#         dict_rate = {
#             "car_id": car_id,
#             "rating": rate,
#         }
#         return JsonResponse(dict_rate)


class PopularCarsView(views.APIView):
    def get(self, request):
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
