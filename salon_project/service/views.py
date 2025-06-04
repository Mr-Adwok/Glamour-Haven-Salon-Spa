from .models import Service
from .serializers import ServiceSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import CustomUser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny


@api_view(["GET"])
@permission_classes([AllowAny])
def all_service(request):
    # serializer = Appointment_Service(request.data)
    my_object = Service.objects.all()
    serializer = ServiceSerializer(my_object,many  = True, context={'request': request})
    return Response(serializer.data)

@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def add_service(request):
    # if request.user.is_customer:
    #     return Response({"detail": "You are not allowed to add services."}, status=status.HTTP_403_FORBIDDEN)
    serializer =  ServiceSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# def all_service(request):
#     services = Service.objects.all()

#     return render(request, 'home.html', {'services': services})



# def home(request):
#     return render(request, 'home.html')