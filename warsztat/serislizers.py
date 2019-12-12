from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        def validate_vin(self, data):
        if len(data['password']) < 8:
            raise serializers.ValidationError("User password must be longer than 8 characters!")
        return data

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        
        def validate_vin(self, data):
        if len(data['VIN']) != 17:
            raise serializers.ValidationError("Vin number must be 17 characters length!")
        return data

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class Invoiceserializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
