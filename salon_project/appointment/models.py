from django.db import models
from service.models import Service

# Create your models here.

class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete = models.DO_NOTHING)
    stylist = models.CharField(max_length  = 200)
    date = models.DateField()
    time = models.TimeField()
    special_request = models.CharField(max_length = 500)


