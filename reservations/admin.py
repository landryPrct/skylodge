from django.contrib import admin

from reservations.models import Chambre, Reservation

admin.site.register(Chambre)
admin.site.register(Reservation)