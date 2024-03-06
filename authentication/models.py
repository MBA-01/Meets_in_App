from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(('email address'), unique = True)
    native_name = models.CharField(max_length = 5)
    phone_number = models.CharField(max_length = 10)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    # to be completed
    # https://www.geeksforgeeks.org/creating-custom-user-model-using-abstractuser-in-django_restframework/
    def __str__(self) :
        return "{}".format(self.email)


