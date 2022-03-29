from django.contrib import admin
from .models import Reservation, Room, Contact
from accounts.models import Customer,Manager,User

# Register your models here.


  # pour afficher dans administartion
admin.site.register(User)
admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Contact)