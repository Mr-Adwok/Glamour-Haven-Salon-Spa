from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id","name", "description", "price", "category", "image", "featured"]
        read_on_fields = ["id"]


