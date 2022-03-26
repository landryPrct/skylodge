from django.db import models
from accounts.models import Manager,Customer
from django.contrib.auth.models import User



# Create your models here.
class Room(models.Model):
    manager=models.ForeignKey(Manager,on_delete=models.CASCADE)
    room_no=models.CharField(max_length=5)
    room_type=models.CharField(max_length=50)
    is_available=models.BooleanField(default=True)
    price=models.IntegerField(default=20000)
    star_date=models.DateField(auto_now=False,auto_now_add=False)


    def __str__(self):
        return str(self.id)



class Reservation(models.Model):  # la Reservation
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_day = models.DateField(auto_now=False, auto_now_add=False)
    end_day = models.DateField(auto_now=False, auto_now_add=False)
    amount = models.FloatField()
    booked_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return  str(self.id)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.name