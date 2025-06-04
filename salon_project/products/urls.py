from django.urls import path
from .views import create_product, get_product




urlpatterns = [
    path("product/", create_product, name="create-product"),
    path("products/", get_product, name="get-products")
]