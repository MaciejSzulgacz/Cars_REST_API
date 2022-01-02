from django.contrib import admin
from django.urls import path
from cars.views import CreateCarView, DeleteCarView, CreateRateView, PopularCarsView, WelcomeView
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars', CreateCarView.as_view(), name='create_car'),
    path('cars/', CreateCarView.as_view(), name='create_car'),
    path('delete/<int:car_id>', DeleteCarView.as_view(), name='delete'),
    path('', WelcomeView.as_view(), name='base'),
    path('rate', CreateRateView.as_view(), name='create_rate'),
    path('rate/', CreateRateView.as_view(), name='create_rate'),
    path('popular', PopularCarsView.as_view(), name='popular_cars'),
    path('popular/', PopularCarsView.as_view(), name='popular_cars'),
]

urlpatterns += router.urls
