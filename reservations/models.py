from django.db import models
import math
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):

    name = models.CharField(max_length=40, unique=True)
    def __str__(self):
        return self.name