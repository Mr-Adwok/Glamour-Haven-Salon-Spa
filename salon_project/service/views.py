from .models import Service
from .serializers import Service_Serializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import CustomUser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(["POST"])
def all_service(request,id):
    # serializer = Appointment_Service(request.data)
    my_object = Service.Objects.all()
    serializer = Service_Serializer(my_object,many  = True)
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_service(request):

    if request.user.is_customer:
        return Response({"detail": "You are not allowed to add services."}, status=status.HTTP_403_FORBIDDEN)
    serializer =  Service_Serializer(data = request.data)
    if serializer.is_valid():
        serializer.save(user = request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# def all_service(request):
#     services = Service.objects.all()

#     return render(request, 'home.html', {'services': services})



# def home(request):
#     return render(request, 'home.html')