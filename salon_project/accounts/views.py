from django.shortcuts import render
from .serializers import SignUp_Serializer,CustomUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser



@api_view(['POST'])
def signup_page(request):
    serializer = SignUp_Serializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_one_user(request,user_id):
    # user = request.user
    try:
        user  = CustomUser.objects.get(pk = user_id)

    except CustomUser.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = CustomUserSerializer(user)
    return Response(serializer.data)


@api_view(["GET"])
def get_all_user(request):
    all_users = CustomUser.objects.all()
    serializer = CustomUserSerializer(data = all_users,many = True)

    return Response(serializer.data)








# def all_users(request):
#     ...













# Create your views here.

# def login_page(request):

#     return render(request,'login.html')




