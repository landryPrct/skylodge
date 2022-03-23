from django.contrib import admin
from .models import Chambre, Reservation, Paiement

# Register your models here.


admin.site.register(Chambre)  # pour afficher dans administartion

admin.site.register(Reservation)
admin.site.register(Paiement)
