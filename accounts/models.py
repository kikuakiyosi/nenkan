from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass



class Tweet(models.Model):
    message = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
