from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
   is_manager=models.BooleanField(default=False)
   is_customer=models.BooleanField(default=False)
   first_name=models.CharField(max_length=100)
   last_name=models.CharField(max_length=100)

   def __str__(self):
        return self.first_name


class Manager(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone = models.CharField(max_length=30)


    def __str__(self):
        return self.phone


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone = models.CharField(max_length=30)
    adress=models.CharField(max_length=100)

    def __str__(self):
        return self.phone