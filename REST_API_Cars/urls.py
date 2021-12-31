"""REST_API_Cars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cars.views import CarView, CreateCarView, DeleteCarView, ListOfCarsView, CreateRateView, ListOfRatesView, RateView
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars', CreateCarView.as_view(), name='create_car'),
    path('cars/', CarView.as_view(), name='car'),
    path('delete', DeleteCarView.as_view(), name='delete'),
    path('', ListOfCarsView.as_view(), name='base'),
    path('rate', CreateRateView.as_view(), name='create_rate'),
    path('list_of_rates', ListOfRatesView.as_view(), name='list_of_rates'),
    path('rate/', RateView.as_view(), name='rate'),
]

urlpatterns += router.urls
