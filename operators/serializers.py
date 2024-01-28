from rest_framework import serializers
from .models import *



class OperatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'