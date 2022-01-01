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
from cars.views import CreateCarView, DeleteCarView, CreateRateView, PopularCarsView, ListOfCarsView
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars', CreateCarView.as_view(), name='create_car'),
    path('cars/', CreateCarView.as_view(), name='create_car'),
    # path('cars/', FindCarView.as_view(), name='find_car'),
    path('delete/<int:car_id>', DeleteCarView.as_view(), name='delete'),
    path('', ListOfCarsView.as_view(), name='base'),
    path('rate', CreateRateView.as_view(), name='create_rate'),
    path('rate/', CreateRateView.as_view(), name='create_rate'),
    # path('list_of_rates', ListOfRatesView.as_view(), name='list_of_rates'),
    # path('rate/', FindRateView.as_view(), name='find_rate'),
    path('popular', PopularCarsView.as_view(), name='popular_cars'),
    path('popular/', PopularCarsView.as_view(), name='popular_cars'),
]

urlpatterns += router.urls
