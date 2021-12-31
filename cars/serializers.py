from rest_framework import serializers
from .models import Car, Rate


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['make', 'model']


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = ['rate', 'cars']
