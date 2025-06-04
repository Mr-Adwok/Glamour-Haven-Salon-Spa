from rest_framework import serializers
from .models import Appointment
from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['user', 'id']



    def create(self, validated_data):
        user = validated_data.pop("user")
        service = validated_data.get("service")
        stylist = validated_data.get("stylist")
        date = validated_data.get("date")
        time = validated_data.get("time")
        special_request = validated_data.get("special_request")

        request = self.context.get("request")
        user = request.user

        appointment = Appointment(service=service, stylist=stylist, date=date, time=time, special_request=special_request)
        appointment.user = user

        appointment.save()


        return appointment