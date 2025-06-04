from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length = 200, null = True )
    is_customer = models.BooleanField(default = True)
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    # objects = CustomUserManager()

    def __str__(self):
        return self.email

# objects = CustomUserManager()