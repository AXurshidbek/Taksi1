from rest_framework import serializers
from .models import *



class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


