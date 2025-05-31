from django.urls import path
from . import views

urlpatterns = [
    path('all-service/',views.all_service),
    path('add-service/',views.add_service)
]