from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    cep = models.CharField(max_length=255)
    complement = models.TextField()
    number_house = models.CharField(max_length=255)
    references = models.TextField()
