from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import Appointment_Serializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def book_appointment(request):

    # if request.method == "POST":
    serializer = Appointment_Serializer(data = request.data)
    if serializer.is_valid():
        serializer.save(user = request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


