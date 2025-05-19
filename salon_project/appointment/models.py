from django.db import models
from service.models import Service

# Create your models here.

class Appointment(models.Model):
    full_name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    phone_number = models.CharField(max_length = 200)
    service = models.ForeignKey(Service, on_delete = models.DO_NOTHING)
    date = models.DateField()
    time = models.TimeField()
    special_request = models.CharField(max_length = 500)
