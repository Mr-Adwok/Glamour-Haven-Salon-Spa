from rest_framework import serializers
from .models import Appointment


class Appointment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['user']