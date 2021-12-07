from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    complement = models.TextField()
    number_house = models.CharField(max_length=255)
    references = models.TextField()
