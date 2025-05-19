from django.shortcuts import render
from django.http import HttpResponse
from .models import Service


def all_service(request):
    services = Service.objects.all()

    return render(request, 'home.html', {'services': services})



def home(request):
    return render(request, 'home.html')