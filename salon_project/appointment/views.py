from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import AppointmentSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Appointment

# Create your views here.
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def book_appointment(request):
    # if request.method == "POST":
    serializer = AppointmentSerializer(data = request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save(user = request.user)
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def all_appoinment(request):
    if request.user.is_customer:
        return  Response({"detail": "You are not allowed to add services."}, status=status.HTTP_403_FORBIDDEN)

    appiontments = Appointment.objects.all()
    serializer = AppointmentSerializer(appiontments,many  = True)
    return Response(serializer.data)


# user, service, stylist, data, time, special_request,
