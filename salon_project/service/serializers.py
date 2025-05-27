from rest_framework import serializers
from .models import Service


class Service_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
