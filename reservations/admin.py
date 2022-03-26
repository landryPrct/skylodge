from django.contrib import admin
from .models import Reservation, Room
from accounts.models import Customer,Manager

# Register your models here.


  # pour afficher dans administartion

admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(Customer)
admin.site.register(Manager)
