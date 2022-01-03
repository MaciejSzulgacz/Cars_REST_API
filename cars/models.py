from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=128)


class Rate(models.Model):
    rate = models.IntegerField()
    car_id = models.ManyToManyField(Car)
