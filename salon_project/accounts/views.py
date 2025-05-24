from django.shortcuts import render
from .serializers import SignUp_Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['POST'])
def signup_page(request):

    if request.method == "POST":
        serializer = SignUp_Serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

















# Create your views here.

# def login_page(request):

#     return render(request,'login.html')




