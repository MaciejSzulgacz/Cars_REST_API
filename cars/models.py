from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)


class Rate(models.Model):
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    car_id = models.ManyToManyField(Car)
