from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


