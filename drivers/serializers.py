from rest_framework import serializers
from .models import *



class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class CarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategory
        fields = '__all__'
