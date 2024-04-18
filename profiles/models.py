#____________________________________________________________________ PROFILES/MODELS.PY
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
