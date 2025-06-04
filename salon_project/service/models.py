from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length=700)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media")
    featured = models.BooleanField(default=False)


    def __str__(self):
        return self.name


