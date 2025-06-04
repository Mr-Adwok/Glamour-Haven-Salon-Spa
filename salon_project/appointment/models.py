from django.db import models
from service.models import Service
from accounts.models import CustomUser

# Create your models here.

class Appointment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.DO_NOTHING)
    service = models.ForeignKey(Service, on_delete = models.DO_NOTHING)
    stylist = models.CharField(max_length  = 200, default="")
    date = models.DateField()
    time = models.TimeField()
    special_request = models.CharField(max_length = 500, blank=True, null=True)


    def __str__(self):
        return self.date


