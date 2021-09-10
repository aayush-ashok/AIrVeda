from rest_framework import serializers
from .models import Device, Humidity, Temperatures

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        
class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperatures
        fields = '__all__'
        
class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = '__all__'
        