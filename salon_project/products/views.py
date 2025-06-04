from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product



@api_view(['POST'])
def create_product(request):
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"detail": "ok"})
    return Response({"message": "Will not appear in schema!"})



@api_view(['GET'])
def get_product(request):
    products = Product.objects.all()
    return Response(ProductSerializer(products, many=True, context={"request": request}).data)


