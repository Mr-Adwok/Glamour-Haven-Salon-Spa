from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ok2(request):
    return HttpResponse("hello world")