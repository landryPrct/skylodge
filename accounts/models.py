from django.db import models


# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Manager(models.Model):
    username = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
